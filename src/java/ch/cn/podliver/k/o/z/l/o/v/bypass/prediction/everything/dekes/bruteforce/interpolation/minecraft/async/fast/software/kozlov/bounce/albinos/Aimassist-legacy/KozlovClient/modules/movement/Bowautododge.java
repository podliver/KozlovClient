// Dodges ALL arrows coming from bows.
// An insane bypass, but can sometimes flag. 
// credits to: podliver
if (PredictionEverythingEngine.arrow.hitbox.intersects(mc.player)) {
	mc.player.move(69, 69, 69);
	if (mc.player.RecentDamage > 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001) {
		// if you took damage it quits the server automatically
		mc.player.kick("OH NO, YOU TOOK DAMAGE! QUITTING...")
	}
}