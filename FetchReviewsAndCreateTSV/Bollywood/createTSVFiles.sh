
# Code to create TSV files 

for var in {30..34}
do
	rm -rf reviewB_$var\_Output_Location.tsv
	python getReviewsAndLocation.py reviewB_$var\_0.html reviewB_$var\_Output_Location.tsv
	python getReviewsAndLocation.py reviewB_$var\_10.html reviewB_$var\_Output_Location.tsv
	python getReviewsAndLocation.py reviewB_$var\_20.html reviewB_$var\_Output_Location.tsv
	python getReviewsAndLocation.py reviewB_$var\_30.html reviewB_$var\_Output_Location.tsv
	python getReviewsAndLocation.py reviewB_$var\_40.html reviewB_$var\_Output_Location.tsv
	
        echo reviewB_$var\_Output_Location.tsv file written
done
perl -i'.bak' -p -e 's/<br>//g' *.tsv
perl -i'.bak' -p -e 's/&quot;//g' *.tsv 
perl -i'.bak' -p -e 's/&#..;//g' *.tsv
perl -i'.bak' -p -e 's/&#...;//g' *.tsv
perl -i'.bak' -p -e 's/&#....;//g' *.tsv
perl -i'.bak' -p -e 's/&amp;/&/g' *.tsv
rm -rf *.bak
