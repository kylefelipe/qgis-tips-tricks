# Comandos bash para importar varios arquivos vetoriais ao PortGIS.
### Atenção:
#### comandos meramente ilustrativos. Vários parâmetros dos comando usados [shp2pgsql](https://postgis.net/docs/using_postgis_dbmanagement.html#shp2pgsql_usage) foram ignorados!
```
for a in *.shp; do echo "Convertentado $a"; shp2pgsql $a schema.table > ${a%.*}.sql; done
# Depois, para cada .SQL:
for b in *.sql; do psql -d iis -f $b; done 
```

### Alguns comentários  

* `${a%.*}` remove a extenção .shp do nome;  
* O processo aqui apresentados podem ser executados de forma seguida usando pipe `|`;
