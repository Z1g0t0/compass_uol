create table tb_vendedor (
    idVendedor      integer primary key,
    nomeVendedor    text,
    sexoVendedor    integer,
    estadoVendedor  text
);

insert into tb_vendedor ( 
    nomeVendedor   , 
    sexoVendedor   , 
    estadoVendedor
)
    select distinct
	    nomeVendedor   , 
            sexoVendedor   , 
            estadoVendedor
    from tb_locacao;