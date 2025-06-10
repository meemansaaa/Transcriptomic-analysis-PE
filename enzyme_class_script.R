library(tidyverse) #loading libraries
install.packages('readxl')
library(readxl)

eggnog <- read_excel("D:/internship_6_months/eggnog/eggnog_for_viz.xlsx") #loading the input file

#extracting the first digit of the enzyme numbers
eggnog_clean <- eggnog %>%
  filter(!is.na(EC)) %>%
  mutate(EC_class = str_extract(EC, "^\\d"))  # First digit of EC

# Mapping EC class numbers to class names
enzyme_class_map <- c(
  "1" = "Oxidoreductase",
  "2" = "Transferase",
  "3" = "Hydrolase",
  "4" = "Lyase",
  "5" = "Isomerase",
  "6" = "Ligase",
  "7" = "Translocase"
)

eggnog_clean <- eggnog_clean %>%
  mutate(Enzyme_Class = enzyme_class_map[EC_class])

#counting the number of each enzymes
enzyme_counts <- eggnog_clean %>%
  count(Enzyme_Class, sort = TRUE)

#Coverting counts to percentages
enzyme_counts <- enzyme_counts %>%
  mutate(percent = round(n / sum(n) * 100, 1),
         label = paste0(Enzyme_Class, ": ", percent, "%"))

#pie-chart viz
ggplot(enzyme_counts, aes(x = "", y = n, fill = Enzyme_Class)) +
  geom_col(width = 1, color = "white") +
  coord_polar(theta = "y") +
  labs(title = "Enzyme Class Distribution in P. emblica Transcriptome") +
  geom_text(aes(label = label), position = position_stack(vjust = 0.5), size = 4) +
  theme_void()
