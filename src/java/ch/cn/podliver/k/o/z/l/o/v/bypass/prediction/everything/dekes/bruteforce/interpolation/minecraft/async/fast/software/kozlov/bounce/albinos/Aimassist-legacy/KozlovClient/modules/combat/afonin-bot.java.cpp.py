# so basically, its a bot (made by Afonin-Anthony) that is making your pvp skills worse!
# features: AutoSosanie, Aimassist-legacy, TeslaCraft anticheat bypass, Jump Reset Velocity, autoclicker 6 cps.

class afonin-bot {
    String feature = "AutoSosanie";
    Boolean afonin-mode = false;
    
    if (feature.equals("AutoSosanie")) {
        if (players.nearest.radius() <= 3) {
            mc.player.reach(0);
        }
        mc.player.chat("EZZZ");
        mc.player.damage(20);
        if (mc.player.gamemode == GameMode.Spectator) {
            mc.player.chat("Тебе просто повезло, лакич!");
        }
    }
    if (feature.equals("Aimassist-legacy") {
        mc.player.ban("Читерство! (КАД)");
    }
    if ((feature.equals("TeslaCraftanticheatbypass") || feature.equals("JumpResetVelocity")) {
        mc.player.ban("Читерство! (ПА)");
    }
    if (feature.equals("AutoClicker6cps") {
        afonin-mode = true;
        if (afonin-mode) {
            mc.player.yaw(-90);
            mc.player.click("6cps");
            mc.player.chat("О НЕЕЕТ ЗАБАНИЛА((( AFONINHACK не помог");
        }
    }
}