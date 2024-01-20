select *
from {{ 
    metrics.calculate(
        metric('expenses'),
        grain='day',
        dimensions=['customer_status']
    )
}}