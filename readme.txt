#abrir nueva ventana
systemctl stop postgresql-11
./cloud_sql_proxy -instances="sistema-pesquero:us-central:bdd-pesqueriajf"=tcp:5432

#Con el entorno virtual activo
export GOOGLE_CLOUD_PROJECT=sistema-pesquero
export USE_CLOUD_SQL_AUTH_PROXY=true
#luego ejecutar migraciones

#fianlomente
gcloud app deploy
