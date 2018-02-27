"""Helpers for Taxonomy module."""
import logging
from pdb import set_trace
from taxonomy.models import (Taxon, HbvName, HbvFamily, HbvGenus)  # HbvSpecies, HbvXref

logger = logging.getLogger(__name__)


def make_family(fam, kingdom_dict, current_dict, publication_dict):
    """Create Taxon nodes for Division, Class, Order and Family from a HbvFamily record.

    Arguments

    fam An object instance of HBvFamily
    kingdom_dict A lookup of Kingdom IDs and corresponding Taxa of rank Kingdom.
    publication_dict A lookup for publication_status
    current_dict A lookup for current
    """
    logger.info("[make_family] Creating family...")

    try:
        lowest_parent = kingdom_dict[fam.kingdom_id]

        if fam.division_nid:
            dd = dict(
                name_id=fam.division_nid,
                name=fam.division_name,
                rank=Taxon.RANK_DIVISION,
                parent=lowest_parent)
            division, created = Taxon.objects.get_or_create(name_id=fam.division_nid, defaults=dd)
            lowest_parent = division
            if not created:
                Taxon.objects.filter(name_id=fam.division_nid).update(**dd)

        if fam.class_nid:
            dd = dict(
                name_id=fam.class_nid,
                name=fam.class_name,
                rank=Taxon.RANK_CLASS,
                parent=lowest_parent)
            clazz, created = Taxon.objects.get_or_create(name_id=fam.class_nid, defaults=dd)
            lowest_parent = clazz
            if not created:
                Taxon.objects.filter(name_id=fam.class_nid).update(**dd)

        if fam.order_nid:
            dd = dict(
                name_id=fam.order_nid,
                name=fam.order_name,
                rank=Taxon.RANK_ORDER,
                parent=lowest_parent)
            order, created = Taxon.objects.get_or_create(name_id=fam.order_nid, defaults=dd)
            lowest_parent = order
            if not created:
                Taxon.objects.filter(name_id=fam.order_nid).update(**dd)

        dd = dict(name_id=fam.name_id,
                  name=fam.family_name,
                  rank=Taxon.RANK_FAMILY,
                  current=current_dict[fam.is_current],
                  parent=lowest_parent)
        if fam.informal is not None:
            dd['publication_status'] = publication_dict[fam.informal]
            print(dd['publication_status'])
        family, created = Taxon.objects.get_or_create(name_id=fam.name_id, defaults=dd)
        if not created:
            Taxon.objects.filter(name_id=fam.name_id).update(**dd)
    except:
        set_trace()

    logger.info("[make_family] Created family {0}.".format(family))
    return family


def make_genus(x, current_dict, publication_dict):
    """Create or update a Taxon of rank Genus.

    Arguments

    x An instance of HbvGenus
    current_dict A lookup dict for is_current

    x:

    'added_on': u'2005-09-06Z',
    'author': u'Saunders',
    'comments': None,
    'editor': None,
    'family_code': u'2037',
    'family_nid': 48499L,
    'genus': u'Hapalospongidion',
    'genusid': 26225L,
    'id': 1352,
    'informal': None,
    'is_current': u'Y',
    'kingdom_id': 6L,
    'md5_rowhash': u'cfe2901a6c7354eb7922a740d29a1d5a',
    'name_id': 26225L,
    'rank_id': 180L,
    'rank_name': u'Genus',
    'reference': u'Erythea 37, Figs 1-4 (1899)',

    Return The created or updated instance of Taxon.
    """
    dd = dict(
        name_id=x.name_id,
        name=x.genus,
        rank=Taxon.RANK_GENUS,
        current=current_dict[x.is_current],
        parent=Taxon.objects.get(name_id=x.family_nid)
    )
    if x.informal is not None:
        dd['publication_status'] = publication_dict[x.informal]

    genus, created = Taxon.objects.get_or_create(name_id=x.name_id, defaults=dd)
    if not created:
        Taxon.objects.filter(name_id=x.name_id).update(**dd)
    action = "Created" if created else "Updated"

    logger.info("[make_genus] {0} genus {1}.".format(action, genus))
    return genus


def update_taxon():
    """Update Taxon from Hbv data."""
    logger.info("[update_taxon] Creating domains...")
    domain, created = Taxon.objects.get_or_create(name_id=0, name="Eukarya", rank=Taxon.RANK_DOMAIN)

    logger.info("[update_taxon] Creating kingdoms...")
    kingdoms = [Taxon.objects.get_or_create(
        name_id=x.name_id, defaults=dict(name=x.name, rank=Taxon.RANK_KINGDOM, parent=domain))
        for x in HbvName.objects.filter(rank_name='Kingdom')]
    logger.info("[update_taxon] Created or updated {0} kingdoms.".format(len(kingdoms)))

    logger.info("[update_taxon] Creating divisions, classes, orders, families...")
    KID = {x.kingdom_id: Taxon.objects.get(name=x.kingdom_name) for x in HbvFamily.objects.all()}
    CURRENT = {'N': False, 'Y': True}
    PUBLICATION = {'PN': 0, 'MS': 1, '-': 2}
    families = [make_family(x, KID, CURRENT, PUBLICATION) for x in HbvFamily.objects.all()]
    logger.info("[update_taxon] Created or updated {0} families and their parentage.".format(len(families)))

    logger.info("[update_taxon] Creating genera...")
    genera = [make_genus(x, CURRENT, PUBLICATION) for x in HbvGenus.objects.all()]

    logger.info("[update_taxon] Created or updated {0} genera.".format(len(genera)))

    logger.info("[update_taxon] Done, exiting.")