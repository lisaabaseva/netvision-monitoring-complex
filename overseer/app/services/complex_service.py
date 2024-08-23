# from typing import List
#
# import requests
#
# from overseer.app.dto.camera import CameraIn, CameraStatusDto
# from overseer.app.exeption import CensusUnavailable
# from overseer.app.config import CENSUS_URL
#
#
# def get_complex_list() -> List[CameraIn]:
#     response = requests.get(CENSUS_URL + "/complexes/")
#
#     if response.status_code != 200:
#         raise CensusUnavailable("Couldn't send complex list request to the census server")
#
#     return response.json()