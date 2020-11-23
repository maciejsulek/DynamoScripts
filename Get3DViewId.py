def Get3DViewId(ViewCol):
	''' Function returns ID of the 3D view. Required to create a new view in Revit. '''
	try:
		for view in ViewCol:
			if view.ViewFamily == ViewFamily.ThreeDimensional:
				ViewId = view.Id
		return ViewId
	except:
		return "Error!"