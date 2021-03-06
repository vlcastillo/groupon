"""
Consulta para analisis de demanda
Cash in primary de deal services por dia
El output se llama cash_in_PDS_por_dia.csv
"""

SELECT  
country.code as country,
opp.Primary_Deal_Services__c as oppPrimary_Deal_Services__c,

YEAR(c.created+interval (if(country.code='AR' and c.created<'2017-08-31 14:00:00', +5,(case country.code when 'AR' then  -3 when 'CL' then -3 when 'CO' then -5 when 'PE' then -5 when 'MX' then  -5 end)+5)) hour) as year_cupon,
MONTH(c.created+interval (if(country.code='AR' and c.created<'2017-08-31 14:00:00', +5,(case country.code when 'AR' then  -3 when 'CL' then -3 when 'CO' then -5 when 'PE' then -5 when 'MX' then  -5 end)+5)) hour) as month_cupon,
day(c.created+interval (if(country.code='AR' and c.created<'2017-08-31 14:00:00', +5,(case country.code when 'AR' then  -3 when 'CL' then -3 when 'CO' then -5 when 'PE' then -5 when 'MX' then  -5 end)+5)) hour) as day_cupon,

count(c.id) as cupones_vendidos,
round(sum(d2.special_price*fx.conversion),2) Cash_in_USD


FROM
	 bi_latam.Fx fx,
	 clandescuento.coupons c #use index(created)
	 LEFT JOIN clandescuento.deals as d on d.id=c.deal_id
	 LEFT JOIN admingroupon.deals as d2  use index (category_id) on d2.id=d.id
     LEFT JOIN admingroupon.deal_partners AS dp ON dp.deal_id = d.id
	 LEFT JOIN admingroupon.countries as country on country.code=d2.country 
	 LEFT JOIN admingroupon.deal_categories as dc ON dc.id=d2.category_id
     LEFT JOIN clandescuento.deal_categories as cdc ON cdc.id=d2.category_id
     left join admingroupon.deals as pd on pd.id=d2.parent_deal_id
     LEFT JOIN bi_latam.categories_bi as bc ON bc.id=d2.category_id
		left join bi_latam.sf_multideal as cda3 on d.salesforce_id= cda3.oldid
		left join bi_latam.sf_multideal as cda2 on d.salesforce_id= cda2.id
		left join bi_latam.sf_multideal as cda on coalesce(cda2.id, cda3.id)= cda.id
		-- left join bi_latam.sf_opportunities as opp on opp.id = cda.Opportunity__c

-- nuevo
		left join bi_latam.sf_opportunities as opp3 on opp3.oldid = d.salesforce_id -- esto es por que el salesfotcr_id apuntan directo a la opp 
        left join bi_latam.sf_opportunities as opp2 on opp2.id = cda.Opportunity__c
        left join bi_latam.sf_opportunities as opp on coalesce(opp2.id,opp3.id) = opp.id
-- nuevo

    
    left join bi_latam.sf_division as divi on divi.id = opp.Division_Dynamic__c  #general


	left join bi_latam.sf_accounts as acc on acc.id = opp.accountid #general
    left join bi_latam.sf_accounts as pacc on acc.ParentId= pacc.id
    LEFT JOIN bi_latam.sf_users as sfu on opp.OwnerId  = sfu.id
        left join bi_latam.sf_users as sfu_acc on acc.OwnerId = sfu_acc.id
 #   left join bi_latam.opp_owner_hist as opph on coalesce(opp.id,opp2.id) = opph.opportunity_id
    # left join bi_latam.socios_nuevos as sn on sn.contract_number = opp.id
    #left join bi_latam.sf_planning as sfp on sfp.deal_id__c = d2.parent_deal_id
	
WHERE
	fx.Fecha='2017-05-01'
	AND fx.country=country.code
    AND country.code in  ('CL','CO','MX','AR','PE')
	AND country.code=d2.country
	AND c.deal_id=d.id
	AND c.status<>'NEW'
	and c.created between '2015-01-01 00:00:00'  and current_date()

group by 1,2,3,4,5

