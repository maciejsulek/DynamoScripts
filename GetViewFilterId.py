def GetViewFilterId(FilterCol, ViewFilterName):
	''' Function returns ID of a phase filter based on the name fed in. Required to set up a view filter in Revit '''
	try:
		for filter in FilterCol:
			if filter.Name == ViewFilterName:
				FilterId = filter.Id			
		return FilterId
	except:
		return "Incorrect Phase Filter Name!"