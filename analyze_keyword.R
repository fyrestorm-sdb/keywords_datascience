###operation reduce sur liste de mots
aggreg_keywords= function(filename){
data=read.csv(filename)
out=head(data,1)
out=out[-1,]## enlever 1er element non necessaire

while(length(data$count)>0){
	v=head(data,1)# toujours travailler sur le premier element de data
	y=subset(data, data$word==v$word)
	v[2]=sum(y$count)
	out=rbind(out,v)
	data=subset(data, data$word!=v$word);
 }

return(out)
}