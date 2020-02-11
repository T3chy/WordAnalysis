library(R.utils)
openPDF <- function(f) {
   os <- .Platform$OS.type
   if (os=="windows")
      shell.exec(normalizePath(f))
   else {
      pdf <- getOption("pdfviewer", default='')
      if (nchar(pdf)==0)
         stop("The 'pdfviewer' option is not set. Use options(pdfviewer=...)")
      system2(pdf, args=c(f))
   }
}
a <- c(scan("/home/t3chy/anaconda3/envs/WordAnalysis/My Scripts/data.txt"))
le <- length(readLines("/home/t3chy/anaconda3/envs/WordAnalysis/My Scripts/data.txt"));
b <- seq(1,le)
print(a)
pdf('/home/t3chy/anaconda3/envs/WordAnalysis/My Scripts/plot.pdf')
#plot.new()
plot(a,col='blue')
abline(lm(a ~ b))
#openPDF('Rplots.pdf')
dev.off() 
# 2. Create a plot
# Close the pdf file

