# R script to save files from a R cisTopic object that can be loaded into pyCisTopic
# USAGE: Rscript cisTopic2pycisTopic.R \
#   /path/to/cisTopic_object.rds \
#   /path/to/output/directory \
#   dataset_name \
#   numTopics \
#   TRUE # subset the number of cells to 100

# Packages
suppressPackageStartupMessages(library(cisTopic))
suppressPackageStartupMessages(library(arrow))

# set random seed for reproducibility
set.seed(12345)

# Read in args
args = commandArgs(trailingOnly = TRUE)
cisTopic_rds = args[1]
outDir = args[2]
dataset_name = args[3]
numTopics = args[4]
subset = args[5]

# Load cisTopic object
print(paste("Loading cisTopic object from", cisTopic_rds))
cisTopic_obj = readRDS(cisTopic_rds)

# Select the correct model for the number of topics
cisTopic_obj <- selectModel(cisTopic_obj, select = numTopics, type="maximum")
modelDims <- dim(cisTopic_obj@selected.model$topics)
print(paste("Selected model with", numTopics, "topics and matrix dimensions of", modelDims[1], "x", modelDims[2]))

### REGION DATA ###

# Save the region probability matrix
regionMatrixPath <- file.path(outDir, paste0(dataset_name, ".regionMat.feather"))
regionMat <- modelMatSelection(cisTopic_obj, 'region', 'Probability', all.regions=TRUE)
regionMat <- as.data.frame(regionMat)
print(paste("Saving region probability matrix with dimensions of", dim(regionMat)[1], "x", dim(regionMat)[2], "to", regionMatrixPath))
write_feather(regionMat, sink=file.path(outDir, paste0(dataset_name, ".regionMat.feather")))
write.table(cisTopic_obj@region.data, file=file.path(outDir, paste0(dataset_name, ".regionData.tsv")), sep="\t", quote=FALSE)

### CELL DATA ###

# Get random barcodes to subset the number of cells to based on the subset argument
if (subset == TRUE) {
    print("Subsetting the number of cells to 100, all objects will be saved with this many cells")
    cells <- sample(rownames(cisTopic_obj@cell.data), 100)
}

# Save the cell probability matrix
cellMatrixPath <- file.path(outDir, paste0(dataset_name, ".cellMat.feather"))
cellMat <- modelMatSelection(cisTopic_obj, 'cell', 'Probability')
if (subset == TRUE) {
    cellMat <- cellMat[, cells]
}
cellMat <- as.data.frame(cellMat)
print(paste("Saving cell probability matrix with dimensions of", dim(cellMat)[1], "x", dim(cellMat)[2], "to", cellMatrixPath))
write_feather(cellMat, sink=file.path(outDir, paste0(dataset_name, ".cellMat.feather")))

# Save the region counts
ctPath <- file.path(outDir, paste0(dataset_name, ".countMatrix.mtx"))
ct <- cisTopic_obj@count.matrix
if (subset == TRUE) {
    ct <- ct[, cells]
}
print(paste("Saving count matrix with dimensions of", dim(ct)[1], "x", dim(ct)[2], "to", ctPath))
Matrix::writeMM(ct, ctPath)

# Save the cell metadata
print(paste("Saving cell metadata to", outDir))
if (subset == TRUE) {
    cellData <- cisTopic_obj@cell.data[cells, ]
} else {
    cellData <- cisTopic_obj@cell.data
}
write.table(cellData, file=file.path(outDir, paste0(dataset_name, ".cellData.tsv")), sep="\t", quote=FALSE)
