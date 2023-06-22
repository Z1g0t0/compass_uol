select tbvendas.cdpro, nmcanalvendas, nmpro, qtd as quantidade_vendas
from tbvendas
left join tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
group by tbvendas.cdpro
limit 10