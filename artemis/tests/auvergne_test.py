from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario


@dataset([DataSet("fr-auv")])
class Auvergne(object):
    """
    test for new_default with data from auvergne
    """
    def test_auvergne_01(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2020
        """
        self.journey(_from="poi:osm:node:303386067",
                     to="3.0630843999999797;45.7589254", datetime="20160121T170000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     max_duration_to_pt=1200)

    def test_auvergne_02(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2016
        """
        self.journey(_from="admin:fr:63135",
                     to="3.121833801269531;45.885276435738504", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     _night_bus_filter_base_factor=7200,
                     max_duration_to_pt=1800)

    def test_auvergne_03(self):
        """
        same that 02, but this time the nigth bus filter should remove walking solution since they are too late
        """
        self.journey(_from="admin:fr:63135",
                     to="3.121833801269531;45.885276435738504", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     _night_bus_filter_base_factor=3600,
                     max_duration_to_pt=1800)

    def test_auvergne_04(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2011
        """
        self.journey(_from="3.0902481079101562;45.8892912569653",
                     to="3.1218767166137695;45.88621444878203", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3)

    def test_auvergne_05(self):
        """
        big PR
        """
        self.journey(_from="3.0902481079101562;45.8892912569653",
                     to="3.1218767166137695;45.88621444878203", datetime="20160118T120300",
                     min_nb_journeys=3)

    def test_geo_status(self):
        """
        check geodata sources and volume
        """
        self.api('_geo_status')

    def test_auvergne_admin_to_station(self):
        """
        test the admin to station
        starts from a small town near Clermont-ferrand to the clermont's station

        The response should be the same for new_default and experimental

        We should be able to:
           * crow fly directly from the main Cebazat stations
           * have a direct path from the center of the town
        """
        self.journey(_from="admin:fr:63063",
                     to="stop_area:SNC:SA:SAOCE87734004", datetime="20160117T120000",
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'])


@set_scenario({"fr-auv": {"scenario": "new_default"}})
class TestAuvergneNewDefault(Auvergne, ArtemisTestFixture):
    pass


@set_scenario({"fr-auv": {"scenario": "experimental"}})
class TestAuvergneExperimental(Auvergne, ArtemisTestFixture):
    pass
