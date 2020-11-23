def UniqueIdToIFCGUID(UniqueId):
    
    ''' 
    This UniqueId can be converted into an IFC GUID by XOR-ing the last 8 characters of the EpisodeId and the 8 character
    ElementId. This provides an IFC GUID in standard UUID format. Revit calls this standard UUID format the "DWF GUID" 
    for historical reasons, but it contains the same data as the IFC GUID. It may then be compressed to the 22-character 
    IFC base64 GlobalId attribute. 
   
    	ElementId = 130315 (Decimal) or 1fd0b (Hex)
    	< ........... EpisodeId .......... >-<ElmtId>
	UniqueId = 60f91daf-3dd7-4283-a86d-24137b73f3da-0001fd0b
    '''
    
    unique_id = UniqueId.replace('-', '')
    dwf_guid = unique_id[0:-16] + hex(int(unique_id[-16:-8], 16) ^ int(unique_id[-8:], 16))[2:]
    ifc_guid = ifcopenshell.guid.compress(dwf_guid)
    return ifc_guid