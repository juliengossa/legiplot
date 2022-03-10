library(tidyverse)
library(ggraph)
library(igraph)


#export("legiplot_load_tree","legiplot_plot_tree")

# Fonctions de chargement
legiplot_load_tree <- function() {
  lp_stats_lts1 <<- legiplot_load_csv("data/lp_stats_lts1.csv")
}


# Arbres
legiplot_plot_tree <- function(lecode) {

  lp_tree <- lp_stats_lts1 %>%
    filter(code==lecode) %>%
    filter(partie == "Législative" | code == "code civil") %>%
    mutate(
      livre = fct_explicit_na(livre, "Sans Livre"),
      titre = fct_explicit_na(titre, "Sans Titre"),
      chapitre = fct_explicit_na(chapitre, "Sans Chapitre")
    ) %>%
    mutate(across(where(is.factor), as.character)) %>%
    mutate(sous_partie = ifelse(sous_partie=="", partie, sous_partie))

  if(n_distinct(lp_tree$sous_partie) > 1) {
    edges <- bind_rows(
      lp_tree %>% group_by(from=code, to=sous_partie) %>% summarise(niveau = 5, groupe="code"),
      lp_tree %>% group_by(from=sous_partie, to=paste(sous_partie,livre)) %>% summarise(niveau = 4, groupe=unique(sous_partie))
    )
  } else {
    edges <-
      lp_tree %>% group_by(from=code, to=paste(sous_partie,livre)) %>% summarise(niveau = 5, groupe="code")
  }

  edges <- bind_rows(edges,
                     lp_tree %>% group_by(from=paste(sous_partie,livre), to=paste(livre,titre)) %>% summarise(niveau = 3, groupe=unique(livre))
  )

  vertices <- bind_rows(
    lp_tree %>% group_by(name = code) %>% summarise(vlabel = unique(code), groupe = "code", niveau = 8, nb_articles = sum(nb_articles)),
    #lp_tree %>% group_by(name = partie) %>% summarise(vlabel = partie, groupe = partie, niveau = 5, nb_articles = sum(nb_articles)),
    #lp_tree %>% group_by(name = sous_partie) %>% summarise(vlabel = unique(sous_partie), groupe = unique(sous_partie), niveau = 4, nb_articles = sum(nb_articles)),
    lp_tree %>% group_by(name = paste(sous_partie,livre)) %>% summarise(vlabel = unique(livre), groupe = unique(livre), niveau = 3, nb_articles = sum(nb_articles)),
    lp_tree %>% group_by(name = paste(livre,titre)) %>% summarise(vlabel = unique(titre), groupe = unique(livre), niveau = 2, nb_articles = sum(nb_articles))
  )

  if(n_distinct(lp_tree$sous_partie) > 1) {
    vertices <- bind_rows(vertices,
                          lp_tree %>% group_by(name = sous_partie) %>% summarise(vlabel = unique(sous_partie), groupe = unique(sous_partie), niveau = 4, nb_articles = sum(nb_articles))
    )
  }

  if (nrow(vertices) > 100) {
    edges <- edges %>% filter(niveau>3)
    vertices <- vertices %>% filter(niveau>2)
  }

  labeller = label_wrap_gen(width = 15)

  mygraph <- graph_from_data_frame(edges,vertices=vertices)
  ggraph(mygraph, layout = 'dendrogram', circular =TRUE)+
    geom_edge_diagonal(aes(colour=groupe))+
    #scale_edge_colour_distiller(palette = "RdPu")+
    geom_node_point(aes(size=nb_articles,colour=groupe))+
    geom_node_text(aes(label=labeller(vlabel)),colour="white",size=vertices$niveau*0.7)+
    scale_size_continuous(range=c(5,50)) +
    theme_void()+
    theme(legend.position="none",plot.margin=unit(c(0,0,0,0),"cm"))
}

# legiplot_load_tree()
# legiplot_plot_tree("code de l'éducation")
