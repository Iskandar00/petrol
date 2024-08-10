from rest_framework.exceptions import ValidationError

from apps.general.enums.districts import DistrictChoices
from apps.general.enums.regions import RegionChoices


def clean(self):
    def clean(self):
        super().clean()

        # Define valid districts for each region
        region_district_map = {
            RegionChoices.ANDIJON: [
                DistrictChoices.ANDIJON,
                DistrictChoices.ASAKA,
                DistrictChoices.BALIQCHI,
                DistrictChoices.BOZORARIK,
                DistrictChoices.BULUNGUR,
                DistrictChoices.JALAQUDIQ,
                DistrictChoices.MARHAMAT,
                DistrictChoices.OLOT,
                DistrictChoices.PAHTAABAD,
                DistrictChoices.XONABAD,
                DistrictChoices.XONQA,
                DistrictChoices.SHAHRIKHON,
                DistrictChoices.SHURABAD,
            ],
            RegionChoices.BUXORO: [
                DistrictChoices.BUXORO,
                DistrictChoices.GIJDUVON,
                DistrictChoices.KOGON,
                DistrictChoices.KARMANA,
                DistrictChoices.VOBKENT,
                DistrictChoices.BUKHARA,
                DistrictChoices.GIZDUVON,
            ],
            RegionChoices.FARGONA: [
                DistrictChoices.FARGONA,
                DistrictChoices.MARGILON,
                DistrictChoices.Qoqon,
                DistrictChoices.RISHTON,
                DistrictChoices.TINCHLIK,
                DistrictChoices.URGANCHI,
            ],
            RegionChoices.JIZZAX: [
                DistrictChoices.JIZZAX,
                DistrictChoices.GALLAOROL,
                DistrictChoices.YANGIYER,
                DistrictChoices.ZANGIOTA,
                DistrictChoices.CHIRCHIK,
            ],
            RegionChoices.XORAZM: [
                DistrictChoices.XIVA,
                DistrictChoices.URGANCH,
                DistrictChoices.SHAVAT,
                DistrictChoices.KHIVA,
            ],
            RegionChoices.NAMANGAN: [
                DistrictChoices.NAMANGAN,
                DistrictChoices.CHORTOQ,
                DistrictChoices.MINGBULAK,
                DistrictChoices.UCHKOPRIK,
            ],
            RegionChoices.NAVOIY: [
                DistrictChoices.NAVOIY,
                DistrictChoices.ZARAFSHON,
                DistrictChoices.QIZILTEPA,
            ],
            RegionChoices.QASHQADARYO: [
                DistrictChoices.QARSHI,
                DistrictChoices.SHAKHRISABZ,
                DistrictChoices.KITAB,
            ],
            RegionChoices.SAMARQAND: [
                DistrictChoices.SAMARQAND,
                DistrictChoices.KATTASAY,
                DistrictChoices.KATTALIK,
            ],
            RegionChoices.SIRDARYO: [
                DistrictChoices.GULISTON,
                DistrictChoices.YANGIYER,
            ],
            RegionChoices.SURXONDARYO: [
                DistrictChoices.TERMIZ,
                DistrictChoices.SHORCHI,
            ],
            RegionChoices.TOSHKENT: [
                DistrictChoices.TOSHkent,
                DistrictChoices.CHIRCHIK,
            ],
            RegionChoices.QORAQALPOGISTON: [
                DistrictChoices.NUKUS,
                DistrictChoices.BERUNIY,
            ],
        }

        # Validate district based on selected region
        if self.district not in region_district_map.get(self.region, []):
            raise ValidationError({
                'district': f"The selected district is not valid for the chosen region '{self.get_region_display()}'."
            })
