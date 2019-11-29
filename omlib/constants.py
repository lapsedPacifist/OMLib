from rdflib import URIRef

from omlib.dimension import Dimension
from omlib.scale import Scale
from omlib.unit import Prefix, Unit


class OM_IDS:
    NAMESPACE = 'http://www.ontology-of-units-of-measure.org/resource/om-2/'
    LENGTH_DIMENSION = URIRef(NAMESPACE + 'length-Dimension')


class SI:
    SYSTEM_OF_UNITS = "SI"  # WARNING If you change "SI" also change in constants.py

    # SI Prefixes
    YOTTA = Prefix('yotta', 'Y', 1e24, OM_IDS.NAMESPACE + 'yotta')
    ZETTA = Prefix('zetta', 'Z', 1e21, OM_IDS.NAMESPACE + 'zetta')
    EXA = Prefix('exa', 'E', 1e18, OM_IDS.NAMESPACE + 'exa')
    PETA = Prefix('peta', 'P', 1e15, OM_IDS.NAMESPACE + 'peta')
    TERA = Prefix('tera', 'T', 1e12, OM_IDS.NAMESPACE + 'tera')
    GIGA = Prefix('giga', 'G', 1e9, OM_IDS.NAMESPACE + 'giga')
    MEGA = Prefix('mega', 'M', 1e6, OM_IDS.NAMESPACE + 'mega')
    KILO = Prefix('kilo', 'k', 1e3, OM_IDS.NAMESPACE + 'kilo')
    HECTO = Prefix('hecto', 'h', 1e2, OM_IDS.NAMESPACE + 'hecto')
    DECA = Prefix('deca', 'da', 1e1, OM_IDS.NAMESPACE + 'deca')
    DECI = Prefix('deci', 'd', 1e-1, OM_IDS.NAMESPACE + 'deci')
    CENTI = Prefix('centi', 'c', 1e-2, OM_IDS.NAMESPACE + 'centi')
    MILLI = Prefix('milli', 'm', 1e-3, OM_IDS.NAMESPACE + 'milli')
    MICRO = Prefix('micro', 'μ', 1e-6, OM_IDS.NAMESPACE + 'micro')
    NANO = Prefix('nano', 'n', 1e-9, OM_IDS.NAMESPACE + 'nano')
    PICO = Prefix('pico', 'p', 1e-12, OM_IDS.NAMESPACE + 'pico')
    FEMTO = Prefix('femto', 'f', 1e-15, OM_IDS.NAMESPACE + 'femto')
    ATTO = Prefix('atto', 'a', 1e-18, OM_IDS.NAMESPACE + 'atto')
    ZEPTO = Prefix('zepto', 'z', 1e-21, OM_IDS.NAMESPACE + 'zepto')
    YOCTO = Prefix('yocto', 'y', 1e-24, OM_IDS.NAMESPACE + 'yocto')

    # SI Base Units
    SECOND = Unit.get_singular_unit('second', 's', Dimension(1, 0, 0, 0, 0, 0, 0),
                                    identifier=OM_IDS.NAMESPACE + 'second',
                                    system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    METRE = Unit.get_singular_unit('metre', 'm', Dimension(0, 1, 0, 0, 0, 0, 0), identifier=OM_IDS.NAMESPACE + 'metre',
                                   system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    GRAM = Unit.get_singular_unit('gram', 'g', Dimension(0, 0, 1, 0, 0, 0, 0), identifier=OM_IDS.NAMESPACE + 'gram')
    KILOGRAM = Unit.get_prefixed_unit(KILO, GRAM, identifier=OM_IDS.NAMESPACE + 'kilogram',
                                      system_of_units=SYSTEM_OF_UNITS,
                                      is_base_unit=True)
    AMPERE = Unit.get_singular_unit('ampere', 'A', Dimension(0, 0, 0, 1, 0, 0, 0),
                                    identifier=OM_IDS.NAMESPACE + 'ampere',
                                    system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    KELVIN = Unit.get_singular_unit('kelvin', 'K', Dimension(0, 0, 0, 0, 1, 0, 0),
                                    identifier=OM_IDS.NAMESPACE + 'kelvin',
                                    system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    MOLE = Unit.get_singular_unit('mole', 'mol', Dimension(0, 0, 0, 0, 0, 1, 0),
                                  identifier=OM_IDS.NAMESPACE + 'mole',
                                  system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    CANDELA = Unit.get_singular_unit('candela', 'cd', Dimension(0, 0, 0, 0, 0, 0, 1),
                                     identifier=OM_IDS.NAMESPACE + 'candela', system_of_units=SYSTEM_OF_UNITS,
                                     is_base_unit=True)


class IEC:
    KIBI = Prefix('kibi', 'Ki', pow(2, 10), OM_IDS.NAMESPACE + 'kibi')
    MEBI = Prefix('mebi', 'Mi', pow(2, 20), OM_IDS.NAMESPACE + 'mebi')
    GIBI = Prefix('gibi', 'Gi', pow(2, 30), OM_IDS.NAMESPACE + 'gibi')
    TEBI = Prefix('tebi', 'Ti', pow(2, 40), OM_IDS.NAMESPACE + 'tebi')
    PEBI = Prefix('pebi', 'Pi', pow(2, 50), OM_IDS.NAMESPACE + 'pebi')
    EXBI = Prefix('exbi', 'Ei', pow(2, 60), OM_IDS.NAMESPACE + 'exbi')
    ZEBI = Prefix('zebi', 'Zi', pow(2, 70), OM_IDS.NAMESPACE + 'zebi')
    YOBI = Prefix('yobi', 'Yi', pow(2, 80), OM_IDS.NAMESPACE + 'yobi')


class JEDEC:
    KILO = Prefix('kilo', 'k', pow(2, 10), OM_IDS.NAMESPACE + 'jedec-kilo')
    MEGA = Prefix('mega', 'M', pow(2, 20), OM_IDS.NAMESPACE + 'jedec-mega')
    GIGA = Prefix('giga', 'G', pow(2, 30), OM_IDS.NAMESPACE + 'jedec-giga')


class IMPERIAL:
    SYSTEM_OF_UNITS = "IMPERIAL"

    # Imperial Base uits
    YARD = Unit.get_singular_unit('yard', 'yd', base_unit=SI.METRE, factor=0.9144, identifier=OM_IDS.NAMESPACE + 'yard',
                                  system_of_units=SYSTEM_OF_UNITS, is_base_unit=True)
    FOOT = Unit.get_singular_unit('foot', 'ft', base_unit=YARD, factor=1/3, identifier=OM_IDS.NAMESPACE + 'foot')
    INCH = Unit.get_singular_unit('inch', 'in', base_unit=YARD, factor=1/36, identifier=OM_IDS.NAMESPACE + 'inch')

    POUND = Unit.get_singular_unit('pound', 'lb', base_unit=SI.KILOGRAM, factor=0.45359237,
                                   identifier=OM_IDS.NAMESPACE + 'pound', system_of_units=SYSTEM_OF_UNITS,
                                   is_base_unit=True)


class OM:
    NAMESPACE = OM_IDS.NAMESPACE
    LENGTH_DIMENSION = OM_IDS.LENGTH_DIMENSION

    ONE = Unit.get_singular_unit("one", "", dimensions=Dimension(), identifier=OM_IDS.NAMESPACE + 'one')

    CENTIMETRE = Unit.get_prefixed_unit(SI.CENTI, base_unit=SI.METRE, identifier=OM_IDS.NAMESPACE + 'centimetre')
    KILOMETRE = Unit.get_prefixed_unit(SI.KILO, base_unit=SI.METRE, identifier=OM_IDS.NAMESPACE + 'kilometre')

    MINUTE_TIME = Unit.get_singular_unit("minute", "m", base_unit=SI.SECOND, factor=60,
                                         identifier=OM_IDS.NAMESPACE + 'minute')
    HOUR_TIME = Unit.get_singular_unit("hour", "h", base_unit=MINUTE_TIME, factor=60,
                                       identifier=OM_IDS.NAMESPACE + 'hour')
    KILOSECOND = Unit.get_prefixed_unit(SI.KILO, base_unit=SI.SECOND, identifier=OM_IDS.NAMESPACE + 'kilosecond')

    DEGREE_CELSIUS = Unit.get_singular_unit("degree Celsius", "°C", base_unit=SI.KELVIN, factor=1.0)
    DEGREE_FAHRENHEIT = Unit.get_singular_unit("degree Fahrenheit", "°F", base_unit=SI.KELVIN, factor=1.0 / 1.8)

    KELVIN_SCALE = Scale.get_ratio_scale(SI.KELVIN, "Kelvin scale", identifier=OM_IDS.NAMESPACE + 'KelvinScale')
    CELSIUS_SCALE = Scale.get_interval_scale(KELVIN_SCALE, DEGREE_CELSIUS, -273.15, "Celsius scale",
                                             identifier=OM_IDS.NAMESPACE + 'CelsiusScale')
    FAHRENHEIT_SCALE = Scale.get_interval_scale(KELVIN_SCALE, DEGREE_FAHRENHEIT, -459.67, "Fahrenheit scale",
                                                identifier=OM_IDS.NAMESPACE + 'FahrenheitScale')

    METRE_PER_SECOND = Unit.get_unit_division(SI.METRE, SI.SECOND, "m/s",
                                              identifier=OM_IDS.NAMESPACE + 'metrePerSecond')
    KILOMETRE_PER_HOUR = Unit.get_unit_division(KILOMETRE, HOUR_TIME, "km/h",
                                                identifier=OM_IDS.NAMESPACE + 'kilometrePerHour')
    METRE_PER_SECOND_SQUARED = Unit.get_unit_division(SI.METRE, Unit.get_unit_exponentiation(SI.SECOND, 2), "m/s2",
                                              identifier=OM_IDS.NAMESPACE + 'metrePerSecondSquared')

    KILOGRAM_METRE_PER_SECOND_SQUARED = Unit.get_unit_multiplication(SI.KILOGRAM, METRE_PER_SECOND_SQUARED,
                                                                     identifier=OM_IDS.NAMESPACE + 'kilogramMetrePerSecond')
    NEWTON = Unit.get_singular_unit('newton', 'N', base_unit=KILOGRAM_METRE_PER_SECOND_SQUARED,
                                    identifier=OM_IDS.NAMESPACE + 'newton')
    JOULE = Unit.get_singular_unit('joule', 'J', base_unit=Unit.get_unit_multiplication(NEWTON, SI.METRE),
                                   identifier=OM_IDS.NAMESPACE + 'joule')
    CALORIE = Unit.get_singular_unit('calorie', 'cal', base_unit=JOULE, factor=4.184,
                                     identifier=OM_IDS.NAMESPACE + 'calorie')
    KILOCALORIE = Unit.get_prefixed_unit(SI.KILO, CALORIE, identifier=OM_IDS.NAMESPACE + 'kilocalorie')
