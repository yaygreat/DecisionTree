Make sure you have installed:
python
pandas
scikit-learn

In your terminal, go to the folder where this file was saved to and type:
	python driver.py

There are 2 data sets you can choose from:
	(1) Iris
	(2) Cars

Select which data set you want to work with and run
to print out the decision trees before and after pruning.

*This driver depends on DecisionTree.py so make sure they're in the same folder.

## Pruning Strategy& Results  
Prune the whole layer above the leaves whenever there exists a majority class. The prediction will be the majority class.If there is not a majority class (there’s an even split), keep the tree as is to avoid ambiguity.    
This strategy will produce a shorter tree with improved or similar accuracy.    
The accuracy will improve when you prune some questions that are not very good data separators, i.e. bad questions that do not reflect an important unique attribute of a class. Near the end of the tree, the best questions are being generated for a specific, smaller set ofdata, which will generatebest info gain at the moment, but it might not be very good info gain, i.e. not a very good question, and thus not an important attribute of the predicted class.    
In the previous pruning strategy, when there is not a majority class it sees that there is more potentialfor another question to help us achieve more info gainwhereas there is less potential to achieveinfo more gainthan we already had from asking another question and so it is pruned.Sometimes the pruning strategy might prune a question that gives good insight into a clear separation of data because this strategy does not check to not prune if the question gives a good info gain. However, this can be remedied by storing the info gain within the nodes and stating not to prune if it is over a specific threshold. This will basically prune out ONLY the not very good questions that do not make the info gain cut.
