"""The Ontario Energy Board component.
"""
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import OntarioEnergyBoardDataUpdateCoordinator


PLATFORMS = [Platform.SENSOR]


async def async_setup_entry(hass, entry: ConfigEntry):
    """Set up the Ontario Energy Board component."""
    hass.data.setdefault(DOMAIN, {})
    coordinator = OntarioEnergyBoardDataUpdateCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
