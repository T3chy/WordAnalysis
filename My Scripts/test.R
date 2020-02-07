
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
a <- c(scan("data.txt"))
b <- seq(1,22)
print(a)
plot.new()
plot(a,col='blue')
abline(lm(a ~ b))
openPDF('Rplots.pdf')