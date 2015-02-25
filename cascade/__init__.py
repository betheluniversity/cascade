
from AssetOperationHandlerService import AssetOperationHandlerService

from cascade import Cascade
from report import Report

wsdl = "http://cms-origin.bethel.edu/ws/services/AssetOperationService?wsdl";
auth = {'tinker': 'v3rQWaJZorT2pAJ'}

service = AssetOperationHandlerService(wsdl, auth)
cascade = Cascade(service)
report = Report(cascade)

from constants.types import T

t = T()

print t.PAGE

print cascade.get_asset(t.PAGE, '2ee211948c5865132b2dadea4f420867')