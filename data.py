USsector = ["All", "Energy", "Technology", "Finance", "Capital Goods", "Health Care", "Consumer Non-Durables", "Basic Industries", "Public Utilities", "Transportation", "Consumer Durables", "Consumer Services", "Miscellaneous"];
tsxvSector = ["All", "Clean Technology", "Comm & Media", "Consumer Products & Services", "CPC", "Financial Services", "Industrial Products & Services", "Life Sciences", "Mining", "Oil & Gas", "Real Estate", "Technology", "Utilities & Pipelines"];
tsxSector = ["All", "Clean Technology", "Closed-End Funds", "Comm & Media", "Consumer Products & Services", "ETP", "Financial Services", "Industrial Products & Services", "Life Sciences", "Mining", "Oil & Gas", "Real Estate", "SPAC", "Technology", "Utilities & Pipelines"];
allCad = ["All", "CPC", "Clean Technology", "Closed-End Funds", "Comm & Media", "Consumer Products & Services", "Diversified Industries", "ETP", "Financial Services", "Industrial Products & Services", "Life Sciences", "Mining", "Oil & Gas", "Real Estate", "SPAC", "Technology", "Utilities & Pipelines"];
cseSector = ["All", "Mining", "Diversified Industries", "Life Sciences", "Technology", "Oil and Gas", "CleanTech"];
allSector = ["All"];
ausSector = ["All", "Capital Goods", "Pharmaceuticals, Biotechnology & Life Sciences", "Food, Beverage & Tobacco", "Materials", "Health Care Equipment & Services", "Energy", "Software & Services", "Commercial & Professional Services", "Consumer Services", "Semiconductors & Semiconductor Equipment", "Telecommunication Services", "Diversified Financials", "Transportation", "Banks", "Real Estate", "Automobiles & Components", "Retailing", "Not Applic", "Media & Entertainment", "Technology Hardware & Equipment", "Utilities", "Consumer Durables & Apparel", "Insurance", "Household & Personal Products", "Food & Staples Retailing", "Class Pend"];
jseSector = ["All", "Technology", "Consumer Goods", "Basic Materials", "Telecommunications", "Financials", "Consumer Services","Health Care", "Industrials", "Oil & Gas"]
egxSector = ['All', 'Banking', 'Chemicals', 'Building Materials/Products', 'Food Products', 'Wholesalers', 'Construction', 'Finance Companies', 'Computer Services', 'Consumer Finance', 'Water Transport/Shipping', 'Oil & Gas Products/Services', 'Healthcare Provision', 'Pharmaceuticals', 'Clothing', 'Real Estate Developers', 'Aluminum', 'Industrial Machinery', 'General Mining', 'Securities', 'Farming', 'Investment Advisors', 'Motor Vehicle Parts', 'Consumer Services', 'Personal Care Products/Appliances', 'Containers/Packaging', 'Full-Line Insurance', 'Tobacco', 'Diversified Holding Companies', 'Hotels', 'Motion Picture/Sound Recording', 'Broadcasting', 'Transportation Services', 'Industrial Products', 'Iron/Steel', 'Tourism', 'Industrial Electronics', 'Diversified Business Services', 'Automobiles', 'Housewares', 'Drug Retail', 'Commercial Vehicles', 'Mixed Retailing', 'Insurance Brokering', 'Oil Extraction', 'Paper/Pulp', 'Software', 'Wired Telecommunications Services'];
bistSector = ['All', 'Chemicals', 'Nondurable Household Products', 'Food Retail', 'Building Materials/Products', 'Non-Alcoholic Beverages/Drinks', 'Life Insurance', 'Banking', 'Diversified Business Services', 'Electric Utilities', 'Hotel/Lodging REITs', 'Clothing', 'Diversified REITs', 'Retail REITs', 'Non-Life Insurance', 'Renewable Energy Generation', 'Networking', 'Paper/Pulp', 'Food Products', 'Hotels', 'Alcoholic Beverages/Drinks', 'Commercial Vehicles', 'Medical Equipment/Supplies', 'Construction', 'Housewares', 'Software', 'Wholesalers', 'Computers/Consumer Electronics', 'Defense Equipment/Products', 'Closed-End Funds', 'Computer Services', 'Gas Utilities', 'Containers/Packaging', 'Motor Vehicle Parts', 'Footwear', 'Diversified Holding Companies', 'Recreational Services', 'General Services', 'Mixed Retailing', 'Environment/Waste Management', 'Iron/Steel', 'Finance Companies', 'Tires', 'Industrial Machinery', 'Fishing', 'Transportation Services', 'Advertising/Marketing/Public Relations', 'Pharmaceuticals', 'Restaurants', 'Publishing', 'Specialty Retail', 'Furniture', 'Industrial Products', 'Printing', 'Industrial Electronics', 'Residential REITs', 'Automobiles', 'Securities', 'Investment Advisors', 'Water Transport/Shipping', 'Real Estate Developers', 'Oil Extraction', 'Industrial/Office REITs', 'Farming', 'Specialty REITs', 'Technical Services', 'Gold', 'Mining Support Services', 'Tourism', 'Healthcare Provision', 'Precision Products', 'Forestry & Wood Products', 'Non-Ferrous Metals', 'Passenger Airlines', 'Consumer Finance', 'Full-Line Insurance', 'Drug Retail', 'Motion Picture/Sound Recording', 'Home Goods Retail', 'Mobile Machinery', 'Oil & Gas Products/Services', 'Major Oil & Gas', 'Passenger Transport, Other', 'Wireless Telecommunications Services', 'Residential Building Construction', 'Multiutilities']


countryObject = {
              "Us": {
                "ALL": USsector,
                "NASDAQ": USsector,
                "NYSE": USsector,
                "AMEX": USsector
              },
              "Canada": {
                "ALL": allCad,
                "TSX": tsxSector,
                "TSXV": tsxvSector,
                "CSE": cseSector, 
                "NEO": allSector
              },
              "Australia": {
                  "ALL": ausSector,                  
                "ASX": ausSector
              },
              "Egypt": {
                  "ALL": egxSector,
                "EGX": egxSector
              },
              "South Africa": {
                  "ALL": jseSector,
                "JSE": jseSector
              },
              "Sweden": {
                  "ALL": allSector,
                "SIX": allSector
              },
              "Turkey": {
                  "ALL": bistSector,
                "BIST": bistSector
              },
            }




         
         
        