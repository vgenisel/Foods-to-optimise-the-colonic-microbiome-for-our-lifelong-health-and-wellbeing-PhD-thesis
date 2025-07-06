#Installing
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("dada2", version = "3.19")


library(dada2); packageVersion("dada2")
library(Biostrings)
library(ggplot2)
library(phyloseq)

path <- "C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_Sequencing/data_16_reduced" # CHANGE ME to the directory containing the fastq files after unzipping.
list.files(path)

# Forward and reverse fastq filenames
fnFs <- sort(list.files(path, pattern="_1.R1.fq", full.names = TRUE))
fnRs <- sort(list.files(path, pattern="_1.R2.fq", full.names = TRUE))

#Removing primers with cutadapt
cutadapt <- "C:/Users/vgenisel/.conda/envs/cutadapt_env/Scripts/cutadapt.exe"
system2(cutadapt, args = "--version") # Run shell commands from R

FWD <- "CCTACGGGAGGCAGCAG"  #forward primer sequence
REV <- "GGACTACHVGGGTWTCTAAT"  #reverse

path.cut <- file.path(path, "cutadapt")
if(!dir.exists(path.cut)) dir.create(path.cut)
fnFs.cut <- file.path(path.cut, basename(fnFs))
fnRs.cut <- file.path(path.cut, basename(fnRs))

FWD.RC <- dada2:::rc(FWD)
REV.RC <- dada2:::rc(REV)

# Trim FWD and the reverse-complement of REV off of R1 (forward reads)
R1.flags <- paste("-g", FWD, "-a", REV.RC) 
# Trim REV and the reverse-complement of FWD off of R2 (reverse reads)
R2.flags <- paste("-G", REV, "-A", FWD.RC) 

# Run Cutadapt
for(i in seq_along(fnFs)) {
  system2(cutadapt, args = c(R1.flags, R2.flags, "-n", 2, # -n 2 required to remove FWD and REV from reads
                             "--minimum-length", 200, "--maximum-length", 250,  #minimum and max lengths    
                             "-o", shQuote(fnFs.cut[i]), "-p", shQuote(fnRs.cut[i]), # output files
                             shQuote(fnFs[i]), shQuote(fnRs[i]))) # input files
}

#Importing trimmed sequences
cutFs <- sort(list.files(path.cut, pattern = "_1.R1.fq", full.names = TRUE))
cutRs <- sort(list.files(path.cut, pattern = "_1.R2.fq", full.names = TRUE))

# Extract sample names
get.sample.name <- function(fname) strsplit(basename(fname), "_")[[1]][1]
sample.names <- unname(sapply(cutFs, get.sample.name))
head(sample.names)

#Checking quality to see where to trim
#plotQualityProfile(cutFs[1:2]) #forward
#plotQualityProfile(cutRs[1:2]) #reverse

filtFs <- file.path(path.cut, "filtered", basename(cutFs))
filtRs <- file.path(path.cut, "filtered", basename(cutRs))
                    

#Filtering and trimming
out <- filterAndTrim(cutFs, filtFs, cutRs, filtRs, truncLen=c(214,195),
                     maxN=213, maxEE=c(2,2), truncQ=2, rm.phix=TRUE,
                     compress=TRUE, multithread=FALSE, verbose=TRUE) # On Windows set multithread=FALSE

head(out)

#Dereplicating
derepF1 <-derepFastq(filtFs,verbose = TRUE)
#derepR1 <-derepFastq(filtRs,verbose = TRUE)

#Error rates
errF <- learnErrors(derepF1, multithread=TRUE)
#errR <- learnErrors(derepR1, multithread=FALSE)
#plotErrors(errF, nominalQ=TRUE)

#Sample inference
dadaFs <- dada(filtFs, err=errF, multithread=TRUE)
dadaFs[[1]]
#dadaRs <- dada(filtRs, err=errR, multithread=TRUE)

#Trying to merge
#mergers <- mergePairs(dadaFs, filtFs, dadaRs, filtRs, verbose=TRUE)

#Sequence table
seqtab <- makeSequenceTable(dadaFs)
dim(seqtab)

table(nchar(getSequences(seqtab))) #inspecting distribution of sequence lengths

#TRacking number of reads through the pipeline
getN <- function(x) sum(getUniques(x))
track <- cbind(out, sapply(dadaFs, getN), rowSums(seqtab))

colnames(track) <- c("input", "filtered", "denoisedF", "nonchim")
rownames(track) <- sample.names
head(track)

#Assing taxonomy
taxa <- assignTaxonomy(seqtab, "C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_Sequencing/silva_nr99_v138.1_wSpecies_train_set.fa.gz", multithread=TRUE)
taxa.print <- taxa # Removing sequence rownames for display only
rownames(taxa.print) <- NULL
head(taxa.print)

#Importing metadata
sampledata <-read.delim("C:/Users/vgenisel/OneDrive - Massey University/Desktop/16S_Sequencing/metadata_reduced.txt",sep = "\t",header = TRUE)

rownames(seqtab) <- sample.names #simplyfing name of samples
rownames(sampledata) <- rownames(seqtab)

#Using phyloseq
ps <- phyloseq(otu_table(seqtab, taxa_are_rows=FALSE), 
               sample_data(sampledata), 
               tax_table(taxa))

dna <- Biostrings::DNAStringSet(taxa_names(ps))
names(dna) <- taxa_names(ps)
ps <- merge_phyloseq(ps, dna)
taxa_names(ps) <- paste0("ASV", seq(ntaxa(ps)))
ps

write.csv(otu_table(ps), "ASV_table.csv")
write.csv(tax_table(ps),"taxatable.csv")
write.csv(refseq(ps),"refseq.csv")
