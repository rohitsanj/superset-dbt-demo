select *
from {{ 
    metrics.calculate(
        metric('profit'),
        grain='day',
        dimensions=['customer_status']
    )
}}