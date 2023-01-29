import arcpy
from arcpy.sa import *

# Establecer el entorno de trabajo
arcpy.env.workspace = r"C:\Datos" # Espacio de trabajo

# Asignar la entrada de raster
inRaster = "2969-25.img" # DEM sobre el que generaremos los ríos
    
# Ejecutar el proceso Fill
outFill = Fill(inRaster)
   
# Ejecutar el proceso FlowDirection
outFlow = FlowDirection(outFill)

# Ejecutar el proceso FlowAccumulation
outAccum = FlowAccumulation(outFlow)
    
# Utilizar la Calculadora de Raster para aplicar la expresión lógica
outLog = Log10(outAccum)
  
# Utilizar la Calculadora de Raster para aplicar la expresión Con
outCon = Con(outLog > 3, outLog)

# Ejecutar la herramienta Stream Link
outStreamLink = StreamLink(outCon, outFlow)

# Ejecutar la herramienta Stream Order
outStreamOrder = StreamOrder(outStreamLink, outFlow)
    
# Ejecutar la herramienta Stream to Feature
outStreamFeature = StreamToFeature(outStreamOrder, outFlow, "rios") # Nombre de la capa de salida
