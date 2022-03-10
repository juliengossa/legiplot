library(tidyverse)
library(ggthemes)
library(cowplot)

#export("legiplot_load_evol","legiplot_ind_plot","legiplot_indcode_plot","legiplot_vol_plot","legiplot_vol_code")

legiplot_load_evol <- function() {
  
  lp_stats <<- legiplot_load_csv("data/lp_diffstats_ts3.csv")
  
  lp_stats_ind <<- lp_stats %>%
    filter(date > as.Date("1810-01-01")) %>% # Gestion d'un problème de nombre de mots dans l'archive
    group_by(code,date,partie) %>%
    summarise(across(nb_articles:nb_mots,sum)) %>%
    mutate(
      alineas_par_article = nb_alineas / nb_articles,
      mots_par_article = nb_mots / nb_articles,
      mots_par_alinea = nb_mots / nb_alineas
    ) 
  
  lp_stats_ind_palette <<- RColorBrewer::brewer.pal(6,"Paired")[c(2,4,6,1,3,5)]
}

# legiplot_load_evol()


# Etude des indicateurs

legiplot_ind_plot <- function(col,collab,norm=FALSE,start="0000-01-01") {
  lp_stats_ind  %>%
    filter(partie == "Législative") %>%
    filter(date >= as.Date(start)) %>%
    mutate(indicateur = !!sym(col)) %>%
    arrange(date) %>%
    group_by(code) %>%
    { if(norm) mutate(., indicateur = indicateur / first(indicateur) * 100) else . } %>%
    ungroup() %>%
    mutate(code = fct_reorder(code,-indicateur,.fun=first)) %>%
    ggplot(aes(x=date,y=indicateur,color=code)) +
    geom_line(aes(group=code)) +
    ylab(collab) +
    theme_hc() + theme(legend.position = "right")
}

# legiplot_ind_plot("nb_mots","Nombre de mots par code")


legiplot_indcode_plot <- function(uncode,start="0001-01-01") {
   
  lp_stats_ind  %>%
    filter(code == uncode & date >= as.Date(start)) %>%
    pivot_longer(-c("code","date","partie"), names_to = "indicateur", values_to = "valeur") %>%
    mutate(indicateur = factor(indicateur, 
      levels = c(
        "nb_articles", "nb_alineas", "nb_mots",
        "alineas_par_article", "mots_par_article", "mots_par_alinea"),
      labels = c(
        "articles", "alineas", "mots",
        "alineas par article", "mots par article", "mots par alinea"))) %>%
    arrange(date) %>%
    group_by(code,partie,indicateur) %>%
    mutate(valeur = valeur / first(valeur) * 100) %>%
    ungroup() %>%
    ggplot(aes(x=date,y=valeur,color=indicateur)) +
    geom_line(aes(group=indicateur)) +
    facet_wrap(.~partie, scales = "free_y") +
    scale_color_manual(values=lp_stats_ind_palette) +
    ylab("Evolution en valeur 100 à l'origine") +
    theme_hc() + theme(legend.position = "right")
}

# legiplot_indcode_plot("code civil")


# Etude des volumes des parties

legiplot_vol_plot <- function(pos="stack",uncode=FALSE,start="2000-01-01") {
  lp_stats_vol %>%
  filter(date >= as.Date(start)) %>%
  { if(uncode != FALSE) filter(.,code == uncode) else . } %>%
  mutate(code = fct_reorder(code,-nb_articles,.fun=first)) %>%
  ggplot(aes(x=date,y=nb_articles,color=partie,fill=partie)) +
    geom_area(aes(group=partie),position=pos) +
    expand_limits(x=as.Date("2000-01-01")) +
    { if(uncode == FALSE) 
      facet_wrap(code~., labeller = label_wrap_gen(width=25), scales = "free_x") } +
    { if(pos == "fill") 
      scale_y_continuous(labels = scales::percent)  } +
    ylab("Nombre d'articles") +
    theme_hc() + theme(legend.position = "top")
}


# Etude des volumes des livres

legiplot_vol_code <- function(uncode) {
  lp_stats %>%
    filter(code == uncode) %>%
    group_by(date,partie,livre.no) %>%
    summarise(across(nb_articles:nb_mots,sum)) %>%
    mutate(livre.no = fct_rev(livre.no)) %>%
    
      ggplot(aes(x=date,y=nb_articles,fill=livre.no)) +
      geom_area(aes(group=livre.no),colour="white",size=0.3) +
      facet_grid(.~partie)  +
      theme_hc() + 
      scale_fill_discrete(name="Livre") +
      ylab("Nombre d'articles") +
      theme(legend.position = "right")
}

#legiplot_vol_code("code de l'éducation")


# 
# legiplot_load_evol()
# 
# 
# start <- "2000-01-01"
# norm <- FALSE
# plot_grid(
#   legiplot_ind_plot("nb_mots","Nombre de mots par code",norm,start),
#   legiplot_ind_plot("nb_alineas","Nombre d'alinéas par code",norm,start),
#   legiplot_ind_plot("nb_articles","Nombre d'articles par code",norm,start),
#   legiplot_ind_plot("alineas_par_article","Nombre d'alinéas par article",norm,start),
#   legiplot_ind_plot("mots_par_article","Nombre de mots par article",norm,start),
#   legiplot_ind_plot("mots_par_alinea","Nombre de mots par alinéas",norm,start)
# )
# 
# 
# norm <- TRUE
# plot_grid(
#   legiplot_ind_plot("nb_mots","Nombre de mots par code",norm,start),
#   legiplot_ind_plot("nb_alineas","Nombre d'alinéas par code",norm,start),
#   legiplot_ind_plot("nb_articles","Nombre d'articles par code",norm,start),
#   legiplot_ind_plot("alineas_par_article","Nombre d'alinéas par article",norm,start),
#   legiplot_ind_plot("mots_par_article","Nombre de mots par article",norm,start),
#   legiplot_ind_plot("mots_par_alinea","Nombre de mots par alinéas",norm,start)
# )

# 
# legiplot_vol_plot()
# 
# legiplot_vol_plot("fill")
# 
# legiplot_vol_plot(pos="fill",uncode="code de l'éducation")
# 
