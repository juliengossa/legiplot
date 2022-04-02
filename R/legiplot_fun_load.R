library(tidyverse)

#export(legiplot_load_csv)
legiplot_load_csv <- function(csvfile) {
  lp <- read.csv(csvfile,encoding = "UTF-8", stringsAsFactors = TRUE) %>%
    mutate(
      code = as.factor(str_replace_all(code,"_"," ")),
      partie = factor(case_when(
        str_detect(partie,"législative|LEGISLATIVE") | partie == "" ~ "Législative",
        code == "code civil" ~ "Législative",
        TRUE ~ "Réglementaire"),
        levels = c("Législative","Réglementaire")),
      date = as.Date(date),
      ) 
  
  if ("livre" %in% colnames(lp)) {
    lp <- lp %>% 
      mutate(livre.no = sapply(str_split(str_replace(livre,"  "," ")," "),"[",2)) %>%
      mutate(livre.num=as.character(as.roman(ifelse(str_detect(livre.no, "^[:digit:]+$"), livre.no, NA))))  %>%
      mutate(livre.no=ifelse(is.na(livre.num), livre.no, livre.num)) %>%
      mutate(livre.no=recode(livre.no, "I" = "Ier","IER" = "Ier")) %>%
      mutate(livre.no=replace_na(livre.no,"hors livre")) %>%
      mutate(livre.no=factor(
        livre.no,
        levels = c("hors livre","préliminaire","Ier",as.character(as.roman(seq(2,20)))) )
        ) %>%
      select(-livre.num)
  }
  
  return(lp)
}

#raw <- legiplot_load_csv("lp_diff_t.csv")


elections = as.Date(paste0(c(1959,1965,1969,1974,1981,1988,1995,2002,2007,2012,2017,2022),"-06-01"))
