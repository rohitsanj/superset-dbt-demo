select *
from {{ 
    metrics.calculate(
        metric('average_order_amount'),
        grain='day',
        dimensions=['customer_status']
    )
}}