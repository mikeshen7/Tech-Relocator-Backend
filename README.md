# Tech Relocator Backend

## Team Members
- Diontre Sanders
- Mike Shen

## Description

Showcase data across the US for Tech Job Market openings within the last year. Allowing users to access skills for those job fields, information for locations.

## Endpoints / search parameters: 

https://tech-relocator-backend.vercel.app/api/v1/users/

https://tech-relocator-backend.vercel.app/api/v1/job_data
- ?title=python
- ?location=seattle
- ?salary=100000
- ?title=python&location=san&salary=100000

https://tech-relocator-backend.vercel.app/api/v1/skills
- ?search=python

https://tech-relocator-backend.vercel.app/api/v1/col
- ?state=washington
- ?state=washington&state=oregon

https://tech-relocator-backend.vercel.app/api/v1/col_city
- ?state=washington
- ?state_code=WA
- ?city=seattle
- ?state_code=washington&state=oregon&state_code=CA&state_code=FL&city=san&city=dallas

https://tech-relocator-backend.vercel.app/token

https://tech-relocator-backend.vercel.app/token/refresh

