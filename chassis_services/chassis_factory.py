from chassis_services.sedan_chassis import SedanChassis
from chassis_services.sport_chassis import SportChassis
from chassis_services.ute_chassis import UteChassis
from order import Chassis


class ChassisFactory:

    def create_chassis(self, chassis_type: Chassis):
        if (chassis_type == Chassis.SPORT):
            return SportChassis()
        elif (chassis_type == Chassis.SEDAN):
            return SedanChassis()
        elif (chassis_type == Chassis.UTE):
            return UteChassis()
        else:
            raise NotImplementedError("Chassis type not implemented")
