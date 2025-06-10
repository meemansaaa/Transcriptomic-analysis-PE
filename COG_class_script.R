library(tidyverse) #loading libraries
install.packages('readxl')
library(readxl)

eggnog2 <- read_excel("D:/internship_6_months/eggnog/eggnog_for_viz.xlsx") #loading the input file

#couting the number of transcripts for each COG category

#cog_counts <- eggnog %>%
  #filter(!is.na(COG)) %>%
  #separate_rows(COG, sep = "") %>%  # splits multiple-letter codes
  #count(COG_category, sort = TRUE)

#mapping each COG, builds a dataframe
cog_map <- tibble::tribble(
  ~COG, ~Description,
  "A", "RNA processing and modification",
  "B", "Chromatin structure and dynamics",
  "C", "Energy production and conversion",
  "D", "Cell cycle control, cell division",
  "E", "Amino acid transport and metabolism",
  "F", "Nucleotide transport and metabolism",
  "G", "Carbohydrate transport and metabolism",
  "H", "Coenzyme transport and metabolism",
  "I", "Lipid transport and metabolism",
  "J", "Translation, ribosomal structure and biogenesis",
  "K", "Transcription",
  "L", "Replication, recombination and repair",
  "M", "Cell wall/membrane/envelope biogenesis",
  "N", "Cell motility",
  "O", "Posttranslational modification, protein turnover",
  "P", "Inorganic ion transport and metabolism",
  "Q", "Secondary metabolites biosynthesis",
  "R", "General function prediction only",
  "S", "Function unknown",
  "T", "Signal transduction mechanisms",
  "U", "Intracellular trafficking and secretion",
  "V", "Defense mechanisms",
  "W", "Extracellular structures",
  "Y", "Nuclear structure",
  "Z", "Cytoskeleton"
)

#filtering with COG, then left joining with the description database (make sure column names match)
cog_counts <- eggnog2 %>%
  filter(!is.na(COG)) %>%
  separate_rows(COG, sep = "") %>%
  count(COG, sort = TRUE) %>%
  left_join(cog_map, by = "COG")

ggplot(cog_counts, aes(x = reorder(Description, n), y = n)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "COG Functional Category Distribution",
       x = "Function",
       y = "Number of Transcripts") +
  theme_minimal()