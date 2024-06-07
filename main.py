from Ingestion.ingestion import * 
from Transformation.transformation import * 
from Querying.querying import * 


def main():
    ingestion()
    finaldf= transformation()
    print(get_people_above_30k(finaldf))
    print(get_repartion_F_H(finaldf))

if __name__ == "__main__":
    main()
