
keywords=function(){
library(ggplot2)
valid_ads=685
data=read.csv("keywords_list_2.csv",sep=",")
u=aggregate(x = data$word,  by = list(word=data$word), FUN = length)
u=u[order(-u$x),]


cols=c(">30",">30",">30",">30",">30",">30",">15",">15",">15",">15",">15",">15",">10",">10",">10",">10",">10",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05",">05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05","<05")

pdf("barplot_final_keywords.pdf")

print( ggplot(data=u, aes(x=reorder(word,x), y=x/valid_ads*100,fill = cols)) +geom_hline(yintercept= 5,linetype="dotted") +geom_hline(yintercept= 10,linetype="dotted")+geom_hline(yintercept= 15,linetype="dotted") +geom_hline(yintercept= 30,linetype="dotted")+geom_hline(yintercept= 50,linetype="dotted")+ geom_bar(stat="identity")+ coord_flip()+ylab("Frequence (%)")+xlab("Mots cles")+scale_fill_manual("%", values = c(">30" = "royalblue", ">15" = "lightskyblue", ">10" = "lightblue",">05" = "lightcyan","<05" = "azure"))+scale_y_continuous(breaks=c(5,10,15,30,40,50))+  theme_minimal()
 )


dev.off()

}


combos =function(top){
library(ggplot2)
valid_ads=685
data=read.csv("combo_keywords_list_2.csv",sep=";")
hj=aggregate(x = data$combo,  by = list(word=data$combo), FUN = length)
hj=hj[order(-hj$x),]
return(head(hj,top))

}

