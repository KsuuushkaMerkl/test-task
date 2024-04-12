from edgedb import create_async_client, AsyncIOClient

edgedb_client: AsyncIOClient = create_async_client("edgedb://edgedb:edgedb@db:5656",
                                                   tls_ca_file="certificates/cert.crt")
