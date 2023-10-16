create table tb_cliente(
    idCliente       integer primary key,
    nomeCliente     text,
    cidadeCliente   text,
    estadoCliente   text,
    paisCliente     text
);

insert into tb_cliente( 
    idCliente      , 
    nomeCliente    , 
    cidadeCliente  , 
    estadoCliente  , 
    paisCliente      
)
    select distinct 
        idCliente      , 
        nomeCliente    , 
        cidadeCliente  , 
        estadoCliente  , 
        paisCliente      
    from tb_locacao;
