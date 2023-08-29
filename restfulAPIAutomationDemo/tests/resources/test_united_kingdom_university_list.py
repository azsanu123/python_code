import requests


class ActivityTests:
    """tests to ensure that 200 ok and activity details is returned for the GET request"""

    def test_get_united_kingdom_university_list_information(self, united_kingdom_university_list_resource):
        url = united_kingdom_university_list_resource
        null = None
        response = requests.get(url)
        assert response.status_code == 200
        actual_response_body = response.json()
        # noinspection PyTypeChecker
        expected_response = dict({[
            {
                "country": "United Kingdom",
                "domains": [
                    "futureworks.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Futureworks",
                "web_pages": [
                    "https://futureworks.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "arts.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of the Arts London",
                "web_pages": [
                    "https://www.arts.ac.uk"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "abdn.ac.uk",
                    "aberdeen.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Aberdeen",
                "web_pages": [
                    "http://www.abdn.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "aber.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales, Aberystwyth",
                "web_pages": [
                    "http://www.aber.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "abertay.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Abertay Dundee",
                "web_pages": [
                    "http://www.abertay.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "aiuniv.edu"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "American InterContinental University - London",
                "web_pages": [
                    "http://www.aiuniv.edu/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "aku.edu"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Aga Khan University",
                "web_pages": [
                    "http://www.aku.edu/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "anglia.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Anglia Ruskin University",
                "web_pages": [
                    "http://www.anglia.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "aston.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Aston University",
                "web_pages": [
                    "http://www.aston.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "aul.edu"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "The American University in London",
                "web_pages": [
                    "http://www.aul.edu/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bangor.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales, Bangor",
                "web_pages": [
                    "http://www.bangor.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bath.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Bath",
                "web_pages": [
                    "http://www.bath.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bathspa.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Bath Spa University",
                "web_pages": [
                    "https://www.bathspa.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bbk.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Birkbeck College, University of London",
                "web_pages": [
                    "http://www.bbk.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bcom.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "British College of Osteopathic Medicine",
                "web_pages": [
                    "http://www.bcom.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bcu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Birmingham City University",
                "web_pages": [
                    "http://www.bcu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "beds.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Bedfordshire",
                "web_pages": [
                    "http://www.beds.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bham.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Birmingham",
                "web_pages": [
                    "http://www.bham.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bolton.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Bolton",
                "web_pages": [
                    "http://www.bolton.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bournemouth.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Bournemouth University",
                "web_pages": [
                    "http://www.bournemouth.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "brad.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Bradford",
                "web_pages": [
                    "http://www.brad.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "brijnet.org"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London School of Jewish Studies",
                "web_pages": [
                    "http://www.brijnet.org/lsjs/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bristol.ac.uk",
                    "bris.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Bristol",
                "web_pages": [
                    "https://www.bristol.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "brookes.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Oxford Brookes University",
                "web_pages": [
                    "http://www.brookes.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "brunel.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Brunel University Uxbridge",
                "web_pages": [
                    "http://www.brunel.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bton.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Brighton",
                "web_pages": [
                    "http://www.bton.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "buck.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Buckingham",
                "web_pages": [
                    "http://www.buck.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "bucks.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Buckinghamshire New University",
                "web_pages": [
                    "http://www.bucks.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "cam.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Cambridge",
                "web_pages": [
                    "http://www.cam.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "camb.linst.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Camberwell College of Arts",
                "web_pages": [
                    "http://www.camb.linst.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "canterbury.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Canterbury Christ Church University",
                "web_pages": [
                    "http://www.canterbury.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "cardiff.ac.uk",
                    "cf.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Cardiff University",
                "web_pages": [
                    "http://www.cardiff.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "chelsea.linst.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Chelsea College of Art and Design",
                "web_pages": [
                    "http://www.chelsea.linst.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "chester.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Chester",
                "web_pages": [
                    "http://www.chester.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "city.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "City University",
                "web_pages": [
                    "http://www.city.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "courtauld.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Courtauld Institute of Art, University of London",
                "web_pages": [
                    "http://www.courtauld.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "coventry.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Coventry University",
                "web_pages": [
                    "http://www.coventry.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "cranfield.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Cranfield University",
                "web_pages": [
                    "http://www.cranfield.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "csm.linst.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Central Saint Martins College of Art & Design",
                "web_pages": [
                    "http://www.csm.linst.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "derby.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Derby",
                "web_pages": [
                    "http://www.derby.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "dmu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "De Montfort University Leicester",
                "web_pages": [
                    "http://www.dmu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "dundee.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Dundee",
                "web_pages": [
                    "http://www.dundee.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "dur.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Durham",
                "web_pages": [
                    "http://www.dur.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "edgehill.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Edge Hill University",
                "web_pages": [
                    "http://www.edgehill.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ed.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Edinburgh",
                "web_pages": [
                    "http://www.ed.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "eselondon.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "European School of Economics",
                "web_pages": [
                    "http://www.eselondon.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "essex.ac.uk",
                    "sx.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Essex",
                "web_pages": [
                    "http://www.essex.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ex.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Exeter",
                "web_pages": [
                    "http://www.ex.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "falmouth.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Falmouth University",
                "web_pages": [
                    "http://www.falmouth.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "gcal.ac.uk",
                    "gcu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Glasgow Caledonian University",
                "web_pages": [
                    "http://www.gcal.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "gla.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Glasgow",
                "web_pages": [
                    "http://www.gla.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "glam.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Glamorgan",
                "web_pages": [
                    "http://www.glam.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "glos.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Gloucestershire",
                "web_pages": [
                    "http://www.glos.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "gold.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Goldsmiths College, University of London",
                "web_pages": [
                    "http://www.gold.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "gre.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Greenwich",
                "web_pages": [
                    "http://www.gre.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "gsa.ac.uk",
                    "student.gsa.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Glasgow School of Art",
                "web_pages": [
                    "http://www.gsa.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "halifaxuni.ac"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Halifax, Birmingham Campus",
                "web_pages": [
                    "http://www.halifaxuni.ac/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "herts.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Hertfordshire",
                "web_pages": [
                    "http://www.herts.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "heythrop.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Heythrop College, University of London",
                "web_pages": [
                    "http://www.heythrop.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "hope.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Liverpool Hope University College",
                "web_pages": [
                    "http://www.hope.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "hud.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Huddersfield",
                "web_pages": [
                    "http://www.hud.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "hull.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Hull",
                "web_pages": [
                    "http://www.hull.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "huron.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Huron University USA in London",
                "web_pages": [
                    "http://www.huron.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "hw.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Heriot-Watt University",
                "web_pages": [
                    "http://www.hw.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "imperial.ac.uk",
                    "ic.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Imperial College London",
                "web_pages": [
                    "http://www.imperial.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ifslearning.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "ifs University College",
                "web_pages": [
                    "http://www.ifslearning.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ihr.sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institue of Historical Research, University of London",
                "web_pages": [
                    "http://ihr.sas.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ihr.sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Commonwealth Studies, University of London",
                "web_pages": [
                    "http://www.ihr.sas.ac.uk/ics/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ioe.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Education, University of London",
                "web_pages": [
                    "http://www.ioe.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "islamiccolleges.com"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "International Colleges of Islamic Science",
                "web_pages": [
                    "http://www.islamiccolleges.com/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "kcl.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "King's College London, University of London",
                "web_pages": [
                    "http://www.kcl.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "keele.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Keele University",
                "web_pages": [
                    "http://www.keele.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "kingston.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Kingston University",
                "web_pages": [
                    "http://www.kingston.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "kolieh.com"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "International Centre for Isclamic Science",
                "web_pages": [
                    "http://www.kolieh.com/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lamp.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales, Lampeter",
                "web_pages": [
                    "http://www.lamp.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lancs.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Lancaster",
                "web_pages": [
                    "http://www.lancs.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lboro.ac.uk",
                    "student.lboro.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Loughborough University",
                "web_pages": [
                    "http://www.lboro.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lbs.lon.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London Business School",
                "web_pages": [
                    "http://www.lbs.lon.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lcst.ac"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London College of Science & Technology",
                "web_pages": [
                    "http://www.lcst.ac/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "le.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Leicester",
                "web_pages": [
                    "http://www.le.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "leeds.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Leeds",
                "web_pages": [
                    "http://www.leeds.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lgu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London Guildhall University",
                "web_pages": [
                    "http://www.lgu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "limt.co.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London Institute of Management and Technology",
                "web_pages": [
                    "http://www.limt.co.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lincoln.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Lincoln",
                "web_pages": [
                    "http://www.lincoln.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "liv.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Liverpool",
                "web_pages": [
                    "http://www.liv.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ljmu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Liverpool John Moores University",
                "web_pages": [
                    "https://www.ljmu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lmu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Leeds Metropolitan University",
                "web_pages": [
                    "http://www.lmu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lon.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of London",
                "web_pages": [
                    "http://www.lon.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "londonmet.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London Metropolitan University",
                "web_pages": [
                    "http://www.londonmet.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lsbf.org.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London School of Business & Finance",
                "web_pages": [
                    "http://www.lsbf.org.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lse.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London School of Economics and Political Science, University of London",
                "web_pages": [
                    "http://www.lse.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "lshtm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "London School of Hygiene & Tropical Medicine, University of London",
                "web_pages": [
                    "http://www.lshtm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "manchester.ac.uk",
                    "mbs.ac.uk",
                    "man.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Manchester",
                "web_pages": [
                    "http://www.manchester.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "mdx.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Middlesex University",
                "web_pages": [
                    "http://www.mdx.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "med.ic.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Imperial College School of Medicine",
                "web_pages": [
                    "http://www.med.ic.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "mmu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "The Manchester Metropolitan University",
                "web_pages": [
                    "http://www.mmu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "napier.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Napier University",
                "web_pages": [
                    "http://www.napier.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ncl.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Newcastle-upon-Tyne",
                "web_pages": [
                    "http://www.ncl.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "newport.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales, Newport",
                "web_pages": [
                    "http://www.newport.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "niu.org.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Newport International University",
                "web_pages": [
                    "http://www.niu.org.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "northampton.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Northampton",
                "web_pages": [
                    "http://www.northampton.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "nottingham.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Nottingham",
                "web_pages": [
                    "http://www.nottingham.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ntu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Nottingham Trent University",
                "web_pages": [
                    "http://www.ntu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "open.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Open University",
                "web_pages": [
                    "http://www.open.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "oxford.ac.uk",
                    "ox.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Oxford",
                "web_pages": [
                    "http://www.ox.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "paisley.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Paisley",
                "web_pages": [
                    "http://www.paisley.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "plymouth.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Plymouth",
                "web_pages": [
                    "http://www.plymouth.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "port.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Portsmouth",
                "web_pages": [
                    "http://www.port.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "qmw.ac.uk",
                    "qmul.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Queen Mary, University of London",
                "web_pages": [
                    "http://www.qmul.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "qub.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "The Queen's University Belfast",
                "web_pages": [
                    "http://www.qub.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ram.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Royal Academy of Music, University of London",
                "web_pages": [
                    "http://www.ram.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "rca.ac.uk",
                    "network.rca.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Royal College of Art",
                "web_pages": [
                    "http://www.rca.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "rcm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Royal College of Music, University of London",
                "web_pages": [
                    "http://www.rcm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "rdg.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Reading",
                "web_pages": [
                    "http://www.rdg.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "rfhsm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Royal Free Hospital School of Medicine, University of London",
                "web_pages": [
                    "http://www.rfhsm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "rgu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "The Robert Gordon University",
                "web_pages": [
                    "http://www.rgu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "royalholloway.ac.uk",
                    "rhbnc.ac.uk",
                    "rh.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Royal Holloway and Bedford New College",
                "web_pages": [
                    "http://www.royalholloway.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "richmond.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Richmond University - The American International University in London",
                "web_pages": [
                    "http://www.richmond.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "roehampton.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Roehampton University of Surrey",
                "web_pages": [
                    "http://www.roehampton.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "salford.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Salford",
                "web_pages": [
                    "http://www.salford.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Advanced Legal Studies, University of London",
                "web_pages": [
                    "http://www.sas.ac.uk/ials/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Classical Studies, University of London",
                "web_pages": [
                    "http://www.sas.ac.uk/icls/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Germanic Studies, University of London",
                "web_pages": [
                    "http://www.sas.ac.uk/igs/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Institute of Latin American Studies, University of London",
                "web_pages": [
                    "http://www.sas.ac.uk/ilas/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Warburg Institute, University of London",
                "web_pages": [
                    "http://www.sas.ac.uk/warburg/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sbu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "South Bank University",
                "web_pages": [
                    "http://www.sbu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "schillerlondon.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Schiller International University, London",
                "web_pages": [
                    "http://www.schillerlondon.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sclondon.ac"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Stratford College London",
                "web_pages": [
                    "http://www.sclondon.ac/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sghms.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Saint George's Hospital Medical School, University of London",
                "web_pages": [
                    "http://www.sghms.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "shef.ac.uk",
                    "sheffield.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Sheffield",
                "web_pages": [
                    "http://www.shef.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "shu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Sheffield Hallam University",
                "web_pages": [
                    "http://www.shu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "smu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Swansea Metropolitan University",
                "web_pages": [
                    "http://www.smu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "soas.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "School of Oriental and African Studies, University of London",
                "web_pages": [
                    "http://www.soas.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "solent.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Southampton Solent University",
                "web_pages": [
                    "http://www.solent.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sothebysinstitutelondon.com"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Sotheby´s Institute of Art - London",
                "web_pages": [
                    "http://www.sothebysinstitutelondon.com/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "soton.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Southampton",
                "web_pages": [
                    "http://www.southampton.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ssees.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "School of Slavonic and East European Studies, University of London",
                "web_pages": [
                    "http://www.ssees.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "staffs.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Staffordshire University",
                "web_pages": [
                    "http://www.staffs.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "st-andrews.ac.uk",
                    "st-and.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of St. Andrews",
                "web_pages": [
                    "https://www.st-andrews.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "stir.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Stirling",
                "web_pages": [
                    "http://www.stir.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "st-patricks.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "St.Patrick's International College, London",
                "web_pages": [
                    "http://www.st-patricks.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "strath.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Strathclyde",
                "web_pages": [
                    "http://www.strath.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sunderland.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Sunderland",
                "web_pages": [
                    "http://www.sunderland.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "surrey.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Surrey",
                "web_pages": [
                    "http://www.surrey.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "sussex.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Sussex",
                "web_pages": [
                    "http://www.sussex.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "swan.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales, Swansea",
                "web_pages": [
                    "http://www.swan.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "tcm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Trinity College of Music",
                "web_pages": [
                    "http://www.tcm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "tees.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Teesside",
                "web_pages": [
                    "http://www.tees.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "trinity-cm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Trinity College Carmarthen",
                "web_pages": [
                    "http://www.trinity-cm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "tvu.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Thames Valley University",
                "web_pages": [
                    "http://www.tvu.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ucl.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University College London, University of London",
                "web_pages": [
                    "http://www.ucl.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uclan.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Central Lancashire",
                "web_pages": [
                    "http://www.uclan.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ucs.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University Campus Suffolk",
                "web_pages": [
                    "http://www.ucs.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uea.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of East Anglia",
                "web_pages": [
                    "http://www.uea.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uel.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of East London",
                "web_pages": [
                    "http://www.uel.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ukc.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Kent at Canterbury",
                "web_pages": [
                    "http://www.ukc.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ulsop.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "School of Pharmacy, University of London",
                "web_pages": [
                    "http://www.ulsop.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "ulst.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Ulster",
                "web_pages": [
                    "http://www.ulst.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "umds.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "United Medical and Dental Schools, University of London",
                "web_pages": [
                    "http://www.umds.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "unl.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of North London",
                "web_pages": [
                    "http://www.unl.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "unn.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Northumbria at Newcastle",
                "web_pages": [
                    "http://www.unn.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uwcm.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales College of Medicine",
                "web_pages": [
                    "http://www.uwcm.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uwe.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of the West of England, Bristol",
                "web_pages": [
                    "http://www.uwe.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "uwic.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales Institute, Cardiff",
                "web_pages": [
                    "http://www.uwic.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "wales.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wales",
                "web_pages": [
                    "http://www.wales.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "warnborough.edu"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Warnborough University",
                "web_pages": [
                    "http://www.warnborough.edu/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "warwick.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Warwick",
                "web_pages": [
                    "http://www.warwick.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "westminster.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Westminster",
                "web_pages": [
                    "http://www.westminster.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "williamgilbert.co.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "William Gilbert College",
                "web_pages": [
                    "http://www.williamgilbert.co.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "wimbledon.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Wimbledon School of Art",
                "web_pages": [
                    "http://www.wimbledon.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "wlv.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Wolverhampton",
                "web_pages": [
                    "http://www.wlv.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "worc.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of Worcester",
                "web_pages": [
                    "http://www.worc.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "york.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "University of York",
                "web_pages": [
                    "http://www.york.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "middlesbro.ac.uk",
                    "mbro.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Middlesbrough College",
                "web_pages": [
                    "https://www.mbro.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "stmarys.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "St Mary's University",
                "web_pages": [
                    "https://www.stmarys.ac.uk/home.aspx"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "leedstrinity.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Leeds Trinity University",
                "web_pages": [
                    "https://www.leedstrinity.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "eastcoast.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "East Coast College",
                "web_pages": [
                    "https://www.eastcoast.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "swansea.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Swansea University",
                "web_pages": [
                    "https://www.swansea.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "yorksj.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "York St. John University",
                "web_pages": [
                    "https://www.yorksj.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "cavc.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Cardiff and Vale College",
                "web_pages": [
                    "https://cavc.ac.uk/"
                ]
            },
            {
                "country": "United Kingdom",
                "domains": [
                    "wakefield.ac.uk"
                ],
                "alpha_two_code": "GB",
                "state-province": null,
                "name": "Wakefield College",
                "web_pages": [
                    "https://wakefield.ac.uk"
                ]
            }
        ]})
        assert actual_response_body == expected_response
