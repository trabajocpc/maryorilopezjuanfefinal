import pandas as pd
from data.platos import platosPopulares
from data.reservas import reservas
from data.creartabla import crearTabla
from data.proovedores import proveedores

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"tablaplatospopulares")

tablaReservas=pd.DataFrame(reservas)
print(tablaReservas)
print(tablaReservas)
crearTabla(tablaReservas,"tablareservas")

TablaProveedores=pd.DataFrame(proveedores)
print(TablaProveedores)
print(tablaReservas)
crearTabla(TablaProveedores,"tablaprovedores")