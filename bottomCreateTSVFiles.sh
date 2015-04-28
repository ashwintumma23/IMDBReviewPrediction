
# Code to create TSV files 

for var in {50..54}
do
	rm -rf review_$var\_Output_Location.tsv
	python getReviewsAndLocation.py review_$var\_0.html review_$var\_Output_Location.tsv
	python getReviewsAndLocation.py review_$var\_10.html review_$var\_Output_Location.tsv
	python getReviewsAndLocation.py review_$var\_20.html review_$var\_Output_Location.tsv
	python getReviewsAndLocation.py review_$var\_30.html review_$var\_Output_Location.tsv
	python getReviewsAndLocation.py review_$var\_40.html review_$var\_Output_Location.tsv
        echo review_$var\_Output_Location.tsv file written
done

