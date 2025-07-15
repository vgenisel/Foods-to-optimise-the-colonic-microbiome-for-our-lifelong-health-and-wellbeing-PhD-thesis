#Loading libraries
import pandas as pd
import scipy
from plotnine import ggplot, aes, geom_point, geom_text, geom_smooth, labs, theme, element_text, element_rect, element_blank, element_line, annotate, guides, guide_legend, facet_grid

#imporitng data
data = pd.read_csv('data_z_scores.csv')

##Evaluating all samples
# Calculate Pearson correlation for each analyte
correlation_results = (
    data.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())
# Extract r and p values and format them
correlation_results.columns = ["Analyte", "Correlation"]
correlation_results["r_value"] = correlation_results["Correlation"].apply(lambda x: x[0])
correlation_results["p_value"] = correlation_results["Correlation"].apply(lambda x: x[1])
correlation_results["correlation_text"] = correlation_results.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data = data.merge(correlation_results[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_all = (
    ggplot(data, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs( title="All samples",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(14, 10),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=8),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_results,
        mapping=aes(x=data["Measured"].max() * 0.3, y=data["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=12,
        color="black",))
plot_all
plot_all.save('results/pearson_correlation_all_samples.svg',dpi = 600)

# Filtering for food and food-food combinations
data = pd.read_csv('data_z_scores.csv')
data_reduced = data[data["Treatment"].isin(["Food", "Food_food"])]

# Calculate Pearson correlation for each analyte
correlation_reduced = (
    data_reduced.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_reduced.columns = ["Analyte", "Correlation"]
correlation_reduced["r_value"] = correlation_reduced["Correlation"].apply(lambda x: x[0])
correlation_reduced["p_value"] = correlation_reduced["Correlation"].apply(lambda x: x[1])
correlation_reduced["correlation_text"] = correlation_reduced.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_reduced = data_reduced.merge(correlation_reduced[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_reduced = (
    ggplot(data_reduced, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs(title="Food ingredients and food-food combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(14, 10),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=8),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_reduced,
        mapping=aes(x=data_reduced["Measured"].max() * 0.3, y=data_reduced["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=12,
        color="black",))
plot_reduced
plot_reduced.save('results/pearson_correlation_food_food-food.svg',dpi = 600)

# Filtering for food-formula and food-food-formula combinations
data = pd.read_csv('data_z_scores.csv')
data_formula = data[data["Treatment"].isin(["Food_formula", "Food_food_formula"])]

# Calculate Pearson correlation for each analyte
correlation_formula = (
    data_formula.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_formula.columns = ["Analyte", "Correlation"]
correlation_formula["r_value"] = correlation_formula["Correlation"].apply(lambda x: x[0])
correlation_formula["p_value"] = correlation_formula["Correlation"].apply(lambda x: x[1])
correlation_formula["correlation_text"] = correlation_formula.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_formula = data_formula.merge(correlation_formula[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_formula = (
    ggplot(data_formula, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs(title="Food-formula and food-food-formula combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(14, 10),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=8),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_formula,
        mapping=aes(x=data_formula["Measured"].max() * 0.3, y=data_formula["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=12,
        color="black",))
plot_formula
plot_formula.save('results/pearson_correlation_formula.svg',dpi = 600)

# Filtering for foods only
data = pd.read_csv('data_z_scores.csv')
data_food = data[data["Treatment"] == "Food"]

# Calculate Pearson correlation for each analyte
correlation_food = (
    data_food.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_food.columns = ["Analyte", "Correlation"]
correlation_food["r_value"] = correlation_food["Correlation"].apply(lambda x: x[0])
correlation_food["p_value"] = correlation_food["Correlation"].apply(lambda x: x[1])
correlation_food["correlation_text"] = correlation_food.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_food = data_food.merge(correlation_food[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_food = (
    ggplot(data_food, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs(title="Food ingredients",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(12, 8),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=12),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_food,
        mapping=aes(x=data_food["Measured"].max() * 0.25, y=data_food["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=13,
        color="black",))
plot_food
plot_food.save('results/pearson_correlation_food.svg',dpi = 600)

# Filtering for food-formula only
data = pd.read_csv('data_z_scores.csv')
data_food_formula = data[data["Treatment"] == "Food_formula"]

# Calculate Pearson correlation for each analyte
correlation_food_formula = (
    data_food_formula.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_food_formula.columns = ["Analyte", "Correlation"]
correlation_food_formula["r_value"] = correlation_food_formula["Correlation"].apply(lambda x: x[0])
correlation_food_formula["p_value"] = correlation_food_formula["Correlation"].apply(lambda x: x[1])
correlation_food_formula["correlation_text"] = correlation_food_formula.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_food_formula = data_food_formula.merge(correlation_food_formula[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_food_formula = (
    ggplot(data_food_formula, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs( title= "Food-formula combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(12, 8),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=11),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_food_formula,
        mapping=aes(x=data_food_formula["Measured"].max() * 0.3, y=data_food_formula["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=13,
        color="black",))
plot_food_formula
plot_food_formula.save('results/person_correlation_food_formula.svg',dpi = 600)

# Filtering for food-food only
data = pd.read_csv('data_z_scores.csv')
data_food_food = data[data["Treatment"] == "Food_food"]

# Calculate Pearson correlation for each analyte
correlation_food_food = (
    data_food_food.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_food_food.columns = ["Analyte", "Correlation"]
correlation_food_food["r_value"] = correlation_food_food["Correlation"].apply(lambda x: x[0])
correlation_food_food["p_value"] = correlation_food_food["Correlation"].apply(lambda x: x[1])
correlation_food_food["correlation_text"] = correlation_food_food.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_food_food = data_food_food.merge(correlation_food_food[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_food_food = (
    ggplot(data_food_food, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs( title="Food-food combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(12, 8),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=12),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + guides(color=guide_legend(ncol=4))  # Split legend into 4 columns
    + geom_text(
        data=correlation_food_food,
        mapping=aes(x=data_food_food["Measured"].max() * 0.2, y=data_food_food["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=13,
        color="black",))
plot_food_food
plot_food_food.save('results/pearson_correlation_food_food.svg',dpi = 600)

# Filtering for food-food-formula only
data = pd.read_csv('data_z_scores.csv')
data_food_food_formula = data[data["Treatment"] == "Food_food_formula"]

# Calculate Pearson correlation for each analyte
correlation_food_food_formula = (
    data_food_food_formula.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_food_food_formula.columns = ["Analyte", "Correlation"]
correlation_food_food_formula["r_value"] = correlation_food_food_formula["Correlation"].apply(lambda x: x[0])
correlation_food_food_formula["p_value"] = correlation_food_food_formula["Correlation"].apply(lambda x: x[1])
correlation_food_food_formula["correlation_text"] = correlation_food_food_formula.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_food_food_formula = data_food_food_formula.merge(correlation_food_food_formula[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_food_food_formula = (
    ggplot(data_food_food_formula, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs( title= "Food-food-formula combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(12, 8),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=11),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + guides(color=guide_legend(ncol=3))  # Split legend into 3 columns
    + geom_text(
        data=correlation_food_food_formula,
        mapping=aes(x=data_food_food_formula["Measured"].max() * 0.3, y=data_food_food_formula["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=13,
        color="black",))
plot_food_food_formula
plot_food_food_formula.save('results/pearson_correlation_food_food_formula.svg',dpi = 600)

#Plant foods only
plant_foods = ["black_beans", "chickpeas", "couscous","blackcurrants", "kumara_with_skin", "kumara_without_skin", "pumpkin", "soybeans", "yellow_peas",
               "raspberries", "strawberries", "black_beans_blackcurrants", "black_beans_pumpkin","blackcurrants_strawberries",
               "blackcurrants_kumara_with_skin", "blackcurrants_kumara_without_skin", "blackcurrants_soybeans", "chickpeas_yellow_peas",
               "couscous_pumpkin", "pumpkin_yellow_peas"]
data = pd.read_csv('data_z_scores.csv')
data_plant = data[data["Sample"].isin(plant_foods)]

# Calculate Pearson correlation for each analyte
correlation_plant = (
    data_plant.groupby("Analyte")
    .apply(lambda df: scipy.stats.pearsonr(df["Measured"], df["Predicted"]))
    .reset_index())

# Extract r and p values and format them
correlation_plant.columns = ["Analyte", "Correlation"]
correlation_plant["r_value"] = correlation_plant["Correlation"].apply(lambda x: x[0])
correlation_plant["p_value"] = correlation_plant["Correlation"].apply(lambda x: x[1])
correlation_plant["correlation_text"] = correlation_plant.apply(
    lambda row: f"r = {row['r_value']:.2f}, p = {row['p_value']:.3f}", axis=1)

# Merge correlation text with the original data
data_plant = data_plant.merge(correlation_plant[["Analyte", "correlation_text"]], on="Analyte", how="left")

# Plotting Z-scored data with facet-wise correlation text
plot_plant = (
    ggplot(data_plant, aes(x="Measured", y="Predicted"))
    + geom_smooth(method="lm", linetype="--")
    + geom_point(aes(color="Sample"), size=3)
    + labs( title= "Plant-based foods and food-food combinations",
        x="Measured Z-score (mmol/gDW.h)",
        y="Predicted Z-score (mmol/gDW.h)",)
    + facet_grid("~Analyte", scales="free")
    + theme(
        figure_size=(14, 10),
        text=element_text(size=18, color="black"),
        panel_background=element_rect(
            fill="white", colour="white", size=0.5, linetype="solid"
        ),
        panel_grid=element_blank(),
        axis_line=element_line(size=2, linetype="solid", colour="black"),
        legend_position="bottom",
        legend_text=element_text(size=8),
        legend_key_size=8,
        axis_text_x=element_text(rotation=45, hjust=1.5),)
    + geom_text(
        data=correlation_plant,
        mapping=aes(x=data_plant["Measured"].max() * 0.3, y=data_plant["Predicted"].max() * 0.9, label="correlation_text"),
        inherit_aes=False,
        size=12,
        color="black",))
plot_plant
plot_plant.save('results/pearson_correlation_plant.svg',dpi = 600)