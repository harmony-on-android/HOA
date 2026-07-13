class UIAbility {
    constructor() {
        this.context = null;
        this.launchWant = null;
    }
    onCreate(want, launchParam) {}
    onDestroy() {}
    onWindowStageCreate(windowStage) {}
    onWindowStageDestroy() {}
    onForeground() {}
    onBackground() {}
    onNewWant(want, launchParam) {}
    onConfigurationUpdate(newConfig) {}
    onMemoryLevel(level) {}
}
export default UIAbility;
