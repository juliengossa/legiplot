
library(tidyverse)
library(ggthemes)

#export("legiplot_load_diff","legiplot_modifs_articles_plot","legiplot_modifs_codes_plot","legiplot_modifs_annees_plot")


legiplot_load_diff <- function() {
  
  lp_modifs <<- legiplot_load_csv("data/lp_diff_t.csv")
  lp_modifs_articles <<- lp_modifs %>%
    filter(type == "Modification") %>%
    group_by(code,partie,sous_partie,livre,titre,chapitre,article) %>%
    summarise(nb_modifications=n())
  
  lp_modifs_articles_sum <<- lp_modifs_articles %>%
    mutate(nb_modifications = factor(
      ifelse(nb_modifications<9,as.character(nb_modifications),"9+")
    )) %>%
    group_by(code,nb_modifications) %>%
    summarise(nb_articles = n())
  
  lp_modifs_annees <<- lp_modifs %>%
    mutate(type = fct_recode(type, Ajout = "Préexistence")) %>%
    mutate(année = as.Date(format(date,"%Y"),"%Y")) %>%
    group_by(code,année,partie,type) %>%
    summarise(nb_articles = n()) %>%
    mutate(type = factor(type,levels = c("Suppression","Modification","Ajout")))

  lp_modifs_codes <<- lp_modifs %>%
    arrange(date) %>%
    mutate(type = fct_recode(type, Ajout = "Préexistence")) %>%
    group_by(code,partie,sous_partie,livre,titre,chapitre,article,type) %>%
    summarise(date=first(date)) %>%
    group_by(code,date,type) %>%
    summarise(nb = n()) %>%
    ungroup() %>%
    complete(nesting(code,date),type, fill = list(nb=0)) %>%
    group_by(code,type) %>%
    mutate(nb = cumsum(nb)) %>%
    ungroup() %>%
    pivot_wider(names_from = type, values_from = nb) %>%
    mutate(Ajout = Ajout - Suppression - Modification) %>%
    pivot_longer(c(Ajout,Suppression,Modification), names_to = "type", values_to = "nb_articles") %>%
    mutate(type = factor(type,levels = c("Suppression","Modification","Ajout"), labels=c("Supprimés","Modififés","Conservés")))
}


legiplot_modifs_articles_plot <- function(uncode=FALSE) {
  lp_modifs_articles_sum %>%
    { if(uncode != FALSE) filter(.,code == uncode) else . } %>%
    ggplot(aes(x=nb_modifications,y=nb_articles,fill=nb_modifications)) +
    geom_col(color="white") +
    { if(uncode == FALSE) 
      facet_wrap(code~., labeller = label_wrap_gen(width=25), scales = "free_y") } +
    xlab("Nombre de modifications") +
    ylab("Nombre d'articles") +
    scale_fill_brewer(palette = "Reds") +
    guides(fill=FALSE) +
    theme_hc() + theme(legend.position = "top")
}


legiplot_modifs_codes_plot <- function(pos="stack",uncode=FALSE,start="2000-01-01", legend.pos="bottom") {
  lp_modifs_codes %>%
    { if(pos != "fill")
      mutate(., nb_articles = ifelse(type=="Supprimés",-nb_articles,nb_articles)) else .} %>%
    filter(date >= as.Date(start)) %>%
    { if(uncode != FALSE) filter(.,code == uncode) else . } %>%
    ggplot(aes(x=date,y=nb_articles,color=type,fill=type)) +
    geom_area(aes(group=type),position=pos, alpha=0.6) +
    geom_line(aes(group=type),position=pos, size=1) +
    { if(uncode == FALSE)
      expand_limits(x=as.Date(start)) } +
    { if(uncode == FALSE) 
      facet_wrap(code~., labeller = label_wrap_gen(width=25), scales = "free_x") } +
    { if(pos == "fill") 
      scale_y_continuous(labels = scales::percent)  } +
    scale_fill_brewer(palette="Set1") +
    scale_color_brewer(palette="Set1") +
    ylab("Nombre d'articles") +
    theme_hc() + theme(legend.position = "bottom") 
}

# legiplot_modifs_codes_plot()
# legiplot_modifs_codes_plot(uncode="code de l'éducation")
# legiplot_modifs_codes_plot(pos="fill",uncode="code de l'éducation")


legiplot_modifs_annees_plot <- function(uncode=FALSE,start="2000-01-01") {
  
  df <- lp_modifs_annees %>% 
    mutate(., nb_articles = ifelse(type=="Suppression",-nb_articles,nb_articles)) %>%
    filter(année >= as.Date(start)) %>%
    { if(uncode != FALSE) filter(.,code == uncode) else . } 
  
  eles <- tibble(début = elections, fin=lead(elections)) %>%
    mutate(al = as.character(row_number() %% 2))
  
    ggplot(df) +
    geom_rect(data=eles,aes(xmin=début,xmax=fin,alpha=al),ymin=-Inf,ymax=Inf,fill="grey") +
    geom_col(aes(x=année,y=nb_articles,color=type,fill=type,group=type), color="white", size=0.3) +
    expand_limits(x=as.Date(start)) +
    { if(uncode == FALSE) 
        facet_wrap(code~., labeller = label_wrap_gen(width=25), scales = "free_x")
      else
        facet_grid(.~partie, labeller = label_wrap_gen(width=25)) } +
    scale_x_continuous(breaks = elections, labels = format(elections, "%Y"), limits = c(min(df$année),max(df$année))) +
    scale_fill_brewer(palette="Set1") +
    scale_alpha_manual(values = c(0.2,0)) +
    ylab("Nombre d'articles") +
    theme_hc() + theme(legend.position = "bottom") + guides(alpha = FALSE)
}

#legiplot_modifs_annees_plot()
#legiplot_modifs_annees_plot("code de l'éducation")


# legiplot_load_diff()
# 
# legiplot_modifs_articles_plot()
# 
# legiplot_modifs_articles_plot("code de l'éducation")
# 
# legiplot_modifs_codes_plot()
# 
# legiplot_modifs_codes_plot(pos="fill")
