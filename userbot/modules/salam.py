from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^\\.kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**PANTEK ASU**")
    sleep(3)
    await typew.edit("`PANTEK PANTEK PANTEK!!!`")
    sleep(3)
    await typew.edit("`DASAR MUKA JELEK!!!`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**DUAR MEMEK**")
    sleep(3)
    await typew.edit("`APA GK SUKA GELUTT!!!`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**DUAR MEMEK**")
    sleep(3)
    await typew.edit("`KALIAN SEMUA ASWWWW!!!`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**ASALAMUALIKUM DULU BIAR SOPAN {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`PUNTENNNN.....`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**ASALAMMUALIKUM DULU BIAR SOPAN {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`PUNTENNNN.....`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`NIH GW JAWAB SALAM LUH KARNA GW ISLAM...`")
    sleep(1)
    await typew.edit("`وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Owner @leaversy


@register(outgoing=True, pattern='^\\.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`NIH GW JAWAB SALAM LU KARNA GW ISLAM...`")
    sleep(1)
    await typew.edit("`وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Owner @leaversy


CMD_HELP.update({
    "salam": "`.P`
    nUsage: Untuk Memberi Hujatan.
    n n`.L`
    nUsage: Untuk Menjawab Salam."
})
