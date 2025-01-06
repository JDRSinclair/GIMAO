import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/TopNavBar.vue";
import { __VLS_internalComponent, __VLS_componentsOption, __VLS_name } from './App.vue';

function __VLS_template() {
let __VLS_ctx!: InstanceType<__VLS_PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_otherComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption;
let __VLS_own!: __VLS_SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & (new () => { $slots: typeof __VLS_slots; })>;
let __VLS_localComponents!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
let __VLS_components!: typeof __VLS_localComponents & __VLS_GlobalComponents & typeof __VLS_ctx;
/* Style Scoped */
type __VLS_StyleScopedClasses = {};
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_resolvedLocalAndGlobalComponents!: {} &
__VLS_WithComponent<'VApp', typeof __VLS_localComponents, "VApp", "vApp", "v-app"> &
__VLS_WithComponent<'NavigationDrawer', typeof __VLS_localComponents, "NavigationDrawer", "NavigationDrawer", "NavigationDrawer"> &
__VLS_WithComponent<'TopNavBar', typeof __VLS_localComponents, "TopNavBar", "TopNavBar", "TopNavBar"> &
__VLS_WithComponent<'VMain', typeof __VLS_localComponents, "VMain", "vMain", "v-main"> &
__VLS_WithComponent<'VContainer', typeof __VLS_localComponents, "VContainer", "vContainer", "v-container"> &
__VLS_WithComponent<'VRow', typeof __VLS_localComponents, "VRow", "vRow", "v-row"> &
__VLS_WithComponent<'VCol', typeof __VLS_localComponents, "VCol", "vCol", "v-col"> &
__VLS_WithComponent<'VCard', typeof __VLS_localComponents, "VCard", "vCard", "v-card"> &
__VLS_WithComponent<'VCardTitle', typeof __VLS_localComponents, "VCardTitle", "vCardTitle", "v-card-title"> &
__VLS_WithComponent<'VDivider', typeof __VLS_localComponents, "VDivider", "vDivider", "v-divider"> &
__VLS_WithComponent<'VList', typeof __VLS_localComponents, "VList", "vList", "v-list"> &
__VLS_WithComponent<'VListItem', typeof __VLS_localComponents, "VListItem", "vListItem", "v-list-item"> &
__VLS_WithComponent<'VListItemTitle', typeof __VLS_localComponents, "VListItemTitle", "vListItemTitle", "v-list-item-title"> &
__VLS_WithComponent<'VDataTable', typeof __VLS_localComponents, "VDataTable", "vDataTable", "v-data-table">;
__VLS_components.VApp; __VLS_components.VApp; __VLS_components.vApp; __VLS_components.vApp; __VLS_components["v-app"]; __VLS_components["v-app"];
// @ts-ignore
[VApp, VApp,];
__VLS_components.NavigationDrawer;
// @ts-ignore
[NavigationDrawer,];
__VLS_components.TopNavBar;
// @ts-ignore
[TopNavBar,];
__VLS_components.VMain; __VLS_components.VMain; __VLS_components.vMain; __VLS_components.vMain; __VLS_components["v-main"]; __VLS_components["v-main"];
// @ts-ignore
[VMain, VMain,];
__VLS_components.VContainer; __VLS_components.VContainer; __VLS_components.vContainer; __VLS_components.vContainer; __VLS_components["v-container"]; __VLS_components["v-container"];
// @ts-ignore
[VContainer, VContainer,];
__VLS_components.VRow; __VLS_components.VRow; __VLS_components.vRow; __VLS_components.vRow; __VLS_components["v-row"]; __VLS_components["v-row"];
// @ts-ignore
[VRow, VRow,];
__VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.VCol; __VLS_components.vCol; __VLS_components.vCol; __VLS_components.vCol; __VLS_components.vCol; __VLS_components["v-col"]; __VLS_components["v-col"]; __VLS_components["v-col"]; __VLS_components["v-col"];
// @ts-ignore
[VCol, VCol, VCol, VCol,];
__VLS_components.VCard; __VLS_components.VCard; __VLS_components.VCard; __VLS_components.VCard; __VLS_components.vCard; __VLS_components.vCard; __VLS_components.vCard; __VLS_components.vCard; __VLS_components["v-card"]; __VLS_components["v-card"]; __VLS_components["v-card"]; __VLS_components["v-card"];
// @ts-ignore
[VCard, VCard, VCard, VCard,];
__VLS_components.VCardTitle; __VLS_components.VCardTitle; __VLS_components.VCardTitle; __VLS_components.VCardTitle; __VLS_components.vCardTitle; __VLS_components.vCardTitle; __VLS_components.vCardTitle; __VLS_components.vCardTitle; __VLS_components["v-card-title"]; __VLS_components["v-card-title"]; __VLS_components["v-card-title"]; __VLS_components["v-card-title"];
// @ts-ignore
[VCardTitle, VCardTitle, VCardTitle, VCardTitle,];
__VLS_components.VDivider; __VLS_components.VDivider; __VLS_components.VDivider; __VLS_components.VDivider; __VLS_components.vDivider; __VLS_components.vDivider; __VLS_components.vDivider; __VLS_components.vDivider; __VLS_components["v-divider"]; __VLS_components["v-divider"]; __VLS_components["v-divider"]; __VLS_components["v-divider"];
// @ts-ignore
[VDivider, VDivider, VDivider, VDivider,];
__VLS_components.VList; __VLS_components.VList; __VLS_components.VList; __VLS_components.VList; __VLS_components.vList; __VLS_components.vList; __VLS_components.vList; __VLS_components.vList; __VLS_components["v-list"]; __VLS_components["v-list"]; __VLS_components["v-list"]; __VLS_components["v-list"];
// @ts-ignore
[VList, VList, VList, VList,];
__VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.VListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components.vListItem; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"]; __VLS_components["v-list-item"];
// @ts-ignore
[VListItem, VListItem, VListItem, VListItem, VListItem, VListItem, VListItem, VListItem,];
__VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.VListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components.vListItemTitle; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"]; __VLS_components["v-list-item-title"];
// @ts-ignore
[VListItemTitle, VListItemTitle, VListItemTitle, VListItemTitle, VListItemTitle, VListItemTitle, VListItemTitle, VListItemTitle,];
__VLS_components.VDataTable; __VLS_components.VDataTable; __VLS_components.vDataTable; __VLS_components.vDataTable; __VLS_components["v-data-table"]; __VLS_components["v-data-table"];
// @ts-ignore
[VDataTable, VDataTable,];
{
const __VLS_0 = ({} as 'VApp' extends keyof typeof __VLS_ctx ? { 'VApp': typeof __VLS_ctx.VApp; } : 'vApp' extends keyof typeof __VLS_ctx ? { 'VApp': typeof __VLS_ctx.vApp; } : 'v-app' extends keyof typeof __VLS_ctx ? { 'VApp': (typeof __VLS_ctx)["v-app"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VApp;
const __VLS_1 = __VLS_asFunctionalComponent(__VLS_0, new __VLS_0({ ...{}, }));
({} as { VApp: typeof __VLS_0; }).VApp;
({} as { VApp: typeof __VLS_0; }).VApp;
const __VLS_2 = __VLS_1({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_1));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_0, typeof __VLS_2> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_3 = __VLS_pickFunctionalComponentCtx(__VLS_0, __VLS_2)!;
let __VLS_4!: __VLS_NormalizeEmits<typeof __VLS_3.emit>;
{
const __VLS_5 = ({} as 'NavigationDrawer' extends keyof typeof __VLS_ctx ? { 'NavigationDrawer': typeof __VLS_ctx.NavigationDrawer; } : typeof __VLS_resolvedLocalAndGlobalComponents).NavigationDrawer;
const __VLS_6 = __VLS_asFunctionalComponent(__VLS_5, new __VLS_5({ ...{ onItemSelected: {} as any, }, logo: ((require('@/assets/images/LogoGIMAO.png'))), items: ((__VLS_ctx.menuItems)), }));
({} as { NavigationDrawer: typeof __VLS_5; }).NavigationDrawer;
const __VLS_7 = __VLS_6({ ...{ onItemSelected: {} as any, }, logo: ((require('@/assets/images/LogoGIMAO.png'))), items: ((__VLS_ctx.menuItems)), }, ...__VLS_functionalComponentArgsRest(__VLS_6));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_5, typeof __VLS_7> & Record<string, unknown>) => void)({ ...{ onItemSelected: {} as any, }, logo: ((require('@/assets/images/LogoGIMAO.png'))), items: ((__VLS_ctx.menuItems)), });
const __VLS_8 = __VLS_pickFunctionalComponentCtx(__VLS_5, __VLS_7)!;
let __VLS_9!: __VLS_NormalizeEmits<typeof __VLS_8.emit>;
let __VLS_10 = { 'item-selected': __VLS_pickEvent(__VLS_9['item-selected'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_6, typeof __VLS_7>).onItemSelected) };
__VLS_10 = { "item-selected": (__VLS_ctx.handleItemSelected) };
}
{
const __VLS_11 = ({} as 'TopNavBar' extends keyof typeof __VLS_ctx ? { 'TopNavBar': typeof __VLS_ctx.TopNavBar; } : typeof __VLS_resolvedLocalAndGlobalComponents).TopNavBar;
const __VLS_12 = __VLS_asFunctionalComponent(__VLS_11, new __VLS_11({ ...{}, }));
({} as { TopNavBar: typeof __VLS_11; }).TopNavBar;
const __VLS_13 = __VLS_12({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_12));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_11, typeof __VLS_13> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_14 = __VLS_pickFunctionalComponentCtx(__VLS_11, __VLS_13)!;
let __VLS_15!: __VLS_NormalizeEmits<typeof __VLS_14.emit>;
}
{
const __VLS_16 = ({} as 'VMain' extends keyof typeof __VLS_ctx ? { 'VMain': typeof __VLS_ctx.VMain; } : 'vMain' extends keyof typeof __VLS_ctx ? { 'VMain': typeof __VLS_ctx.vMain; } : 'v-main' extends keyof typeof __VLS_ctx ? { 'VMain': (typeof __VLS_ctx)["v-main"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VMain;
const __VLS_17 = __VLS_asFunctionalComponent(__VLS_16, new __VLS_16({ ...{}, }));
({} as { VMain: typeof __VLS_16; }).VMain;
({} as { VMain: typeof __VLS_16; }).VMain;
const __VLS_18 = __VLS_17({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_17));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_16, typeof __VLS_18> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_19 = __VLS_pickFunctionalComponentCtx(__VLS_16, __VLS_18)!;
let __VLS_20!: __VLS_NormalizeEmits<typeof __VLS_19.emit>;
{
const __VLS_21 = ({} as 'VContainer' extends keyof typeof __VLS_ctx ? { 'VContainer': typeof __VLS_ctx.VContainer; } : 'vContainer' extends keyof typeof __VLS_ctx ? { 'VContainer': typeof __VLS_ctx.vContainer; } : 'v-container' extends keyof typeof __VLS_ctx ? { 'VContainer': (typeof __VLS_ctx)["v-container"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VContainer;
const __VLS_22 = __VLS_asFunctionalComponent(__VLS_21, new __VLS_21({ ...{}, }));
({} as { VContainer: typeof __VLS_21; }).VContainer;
({} as { VContainer: typeof __VLS_21; }).VContainer;
const __VLS_23 = __VLS_22({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_22));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_21, typeof __VLS_23> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_24 = __VLS_pickFunctionalComponentCtx(__VLS_21, __VLS_23)!;
let __VLS_25!: __VLS_NormalizeEmits<typeof __VLS_24.emit>;
{
const __VLS_26 = ({} as 'VRow' extends keyof typeof __VLS_ctx ? { 'VRow': typeof __VLS_ctx.VRow; } : 'vRow' extends keyof typeof __VLS_ctx ? { 'VRow': typeof __VLS_ctx.vRow; } : 'v-row' extends keyof typeof __VLS_ctx ? { 'VRow': (typeof __VLS_ctx)["v-row"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VRow;
const __VLS_27 = __VLS_asFunctionalComponent(__VLS_26, new __VLS_26({ ...{}, }));
({} as { VRow: typeof __VLS_26; }).VRow;
({} as { VRow: typeof __VLS_26; }).VRow;
const __VLS_28 = __VLS_27({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_27));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_26, typeof __VLS_28> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_29 = __VLS_pickFunctionalComponentCtx(__VLS_26, __VLS_28)!;
let __VLS_30!: __VLS_NormalizeEmits<typeof __VLS_29.emit>;
{
const __VLS_31 = ({} as 'VCol' extends keyof typeof __VLS_ctx ? { 'VCol': typeof __VLS_ctx.VCol; } : 'vCol' extends keyof typeof __VLS_ctx ? { 'VCol': typeof __VLS_ctx.vCol; } : 'v-col' extends keyof typeof __VLS_ctx ? { 'VCol': (typeof __VLS_ctx)["v-col"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCol;
const __VLS_32 = __VLS_asFunctionalComponent(__VLS_31, new __VLS_31({ ...{}, cols: ("3"), }));
({} as { VCol: typeof __VLS_31; }).VCol;
({} as { VCol: typeof __VLS_31; }).VCol;
const __VLS_33 = __VLS_32({ ...{}, cols: ("3"), }, ...__VLS_functionalComponentArgsRest(__VLS_32));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_31, typeof __VLS_33> & Record<string, unknown>) => void)({ ...{}, cols: ("3"), });
const __VLS_34 = __VLS_pickFunctionalComponentCtx(__VLS_31, __VLS_33)!;
let __VLS_35!: __VLS_NormalizeEmits<typeof __VLS_34.emit>;
{
const __VLS_36 = ({} as 'VCard' extends keyof typeof __VLS_ctx ? { 'VCard': typeof __VLS_ctx.VCard; } : 'vCard' extends keyof typeof __VLS_ctx ? { 'VCard': typeof __VLS_ctx.vCard; } : 'v-card' extends keyof typeof __VLS_ctx ? { 'VCard': (typeof __VLS_ctx)["v-card"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCard;
const __VLS_37 = __VLS_asFunctionalComponent(__VLS_36, new __VLS_36({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2 mb-4"), }));
({} as { VCard: typeof __VLS_36; }).VCard;
({} as { VCard: typeof __VLS_36; }).VCard;
const __VLS_38 = __VLS_37({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2 mb-4"), }, ...__VLS_functionalComponentArgsRest(__VLS_37));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_36, typeof __VLS_38> & Record<string, unknown>) => void)({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2 mb-4"), });
const __VLS_39 = __VLS_pickFunctionalComponentCtx(__VLS_36, __VLS_38)!;
let __VLS_40!: __VLS_NormalizeEmits<typeof __VLS_39.emit>;
{
const __VLS_41 = ({} as 'VCardTitle' extends keyof typeof __VLS_ctx ? { 'VCardTitle': typeof __VLS_ctx.VCardTitle; } : 'vCardTitle' extends keyof typeof __VLS_ctx ? { 'VCardTitle': typeof __VLS_ctx.vCardTitle; } : 'v-card-title' extends keyof typeof __VLS_ctx ? { 'VCardTitle': (typeof __VLS_ctx)["v-card-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCardTitle;
const __VLS_42 = __VLS_asFunctionalComponent(__VLS_41, new __VLS_41({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), }));
({} as { VCardTitle: typeof __VLS_41; }).VCardTitle;
({} as { VCardTitle: typeof __VLS_41; }).VCardTitle;
const __VLS_43 = __VLS_42({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), }, ...__VLS_functionalComponentArgsRest(__VLS_42));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_41, typeof __VLS_43> & Record<string, unknown>) => void)({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), });
const __VLS_44 = __VLS_pickFunctionalComponentCtx(__VLS_41, __VLS_43)!;
let __VLS_45!: __VLS_NormalizeEmits<typeof __VLS_44.emit>;
(__VLS_44.slots!).default;
}
{
const __VLS_46 = ({} as 'VDivider' extends keyof typeof __VLS_ctx ? { 'VDivider': typeof __VLS_ctx.VDivider; } : 'vDivider' extends keyof typeof __VLS_ctx ? { 'VDivider': typeof __VLS_ctx.vDivider; } : 'v-divider' extends keyof typeof __VLS_ctx ? { 'VDivider': (typeof __VLS_ctx)["v-divider"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VDivider;
const __VLS_47 = __VLS_asFunctionalComponent(__VLS_46, new __VLS_46({ ...{}, }));
({} as { VDivider: typeof __VLS_46; }).VDivider;
({} as { VDivider: typeof __VLS_46; }).VDivider;
const __VLS_48 = __VLS_47({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_47));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_46, typeof __VLS_48> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_49 = __VLS_pickFunctionalComponentCtx(__VLS_46, __VLS_48)!;
let __VLS_50!: __VLS_NormalizeEmits<typeof __VLS_49.emit>;
}
{
const __VLS_51 = ({} as 'VList' extends keyof typeof __VLS_ctx ? { 'VList': typeof __VLS_ctx.VList; } : 'vList' extends keyof typeof __VLS_ctx ? { 'VList': typeof __VLS_ctx.vList; } : 'v-list' extends keyof typeof __VLS_ctx ? { 'VList': (typeof __VLS_ctx)["v-list"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VList;
const __VLS_52 = __VLS_asFunctionalComponent(__VLS_51, new __VLS_51({ ...{}, dense: (true), }));
({} as { VList: typeof __VLS_51; }).VList;
({} as { VList: typeof __VLS_51; }).VList;
const __VLS_53 = __VLS_52({ ...{}, dense: (true), }, ...__VLS_functionalComponentArgsRest(__VLS_52));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_51, typeof __VLS_53> & Record<string, unknown>) => void)({ ...{}, dense: (true), });
const __VLS_54 = __VLS_pickFunctionalComponentCtx(__VLS_51, __VLS_53)!;
let __VLS_55!: __VLS_NormalizeEmits<typeof __VLS_54.emit>;
{
const __VLS_56 = ({} as 'VListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.VListItem; } : 'vListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.vListItem; } : 'v-list-item' extends keyof typeof __VLS_ctx ? { 'VListItem': (typeof __VLS_ctx)["v-list-item"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItem;
const __VLS_57 = __VLS_asFunctionalComponent(__VLS_56, new __VLS_56({ ...{ onClick: {} as any, }, }));
({} as { VListItem: typeof __VLS_56; }).VListItem;
({} as { VListItem: typeof __VLS_56; }).VListItem;
const __VLS_58 = __VLS_57({ ...{ onClick: {} as any, }, }, ...__VLS_functionalComponentArgsRest(__VLS_57));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_56, typeof __VLS_58> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, });
const __VLS_59 = __VLS_pickFunctionalComponentCtx(__VLS_56, __VLS_58)!;
let __VLS_60!: __VLS_NormalizeEmits<typeof __VLS_59.emit>;
let __VLS_61 = { 'click': __VLS_pickEvent(__VLS_60['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_57, typeof __VLS_58>).onClick) };
__VLS_61 = {
click: $event => {
__VLS_ctx.selectSalle('tous');
// @ts-ignore
[menuItems, menuItems, menuItems, handleItemSelected, selectSalle,];
}
};
{
const __VLS_62 = ({} as 'VListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.VListItemTitle; } : 'vListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.vListItemTitle; } : 'v-list-item-title' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': (typeof __VLS_ctx)["v-list-item-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItemTitle;
const __VLS_63 = __VLS_asFunctionalComponent(__VLS_62, new __VLS_62({ ...{}, }));
({} as { VListItemTitle: typeof __VLS_62; }).VListItemTitle;
({} as { VListItemTitle: typeof __VLS_62; }).VListItemTitle;
const __VLS_64 = __VLS_63({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_63));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_62, typeof __VLS_64> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_65 = __VLS_pickFunctionalComponentCtx(__VLS_62, __VLS_64)!;
let __VLS_66!: __VLS_NormalizeEmits<typeof __VLS_65.emit>;
(__VLS_65.slots!).default;
}
(__VLS_59.slots!).default;
}
for (const [salle] of __VLS_getVForSourceType((__VLS_ctx.salles)!)) {
{
const __VLS_67 = ({} as 'VListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.VListItem; } : 'vListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.vListItem; } : 'v-list-item' extends keyof typeof __VLS_ctx ? { 'VListItem': (typeof __VLS_ctx)["v-list-item"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItem;
const __VLS_68 = __VLS_asFunctionalComponent(__VLS_67, new __VLS_67({ ...{ onClick: {} as any, }, key: ((salle.id)), }));
({} as { VListItem: typeof __VLS_67; }).VListItem;
({} as { VListItem: typeof __VLS_67; }).VListItem;
const __VLS_69 = __VLS_68({ ...{ onClick: {} as any, }, key: ((salle.id)), }, ...__VLS_functionalComponentArgsRest(__VLS_68));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_67, typeof __VLS_69> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, key: ((salle.id)), });
const __VLS_70 = __VLS_pickFunctionalComponentCtx(__VLS_67, __VLS_69)!;
let __VLS_71!: __VLS_NormalizeEmits<typeof __VLS_70.emit>;
let __VLS_72 = { 'click': __VLS_pickEvent(__VLS_71['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_68, typeof __VLS_69>).onClick) };
__VLS_72 = {
click: $event => {
__VLS_ctx.selectSalle(salle.id);
// @ts-ignore
[salles, selectSalle,];
}
};
{
const __VLS_73 = ({} as 'VListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.VListItemTitle; } : 'vListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.vListItemTitle; } : 'v-list-item-title' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': (typeof __VLS_ctx)["v-list-item-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItemTitle;
const __VLS_74 = __VLS_asFunctionalComponent(__VLS_73, new __VLS_73({ ...{}, }));
({} as { VListItemTitle: typeof __VLS_73; }).VListItemTitle;
({} as { VListItemTitle: typeof __VLS_73; }).VListItemTitle;
const __VLS_75 = __VLS_74({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_74));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_73, typeof __VLS_75> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_76 = __VLS_pickFunctionalComponentCtx(__VLS_73, __VLS_75)!;
let __VLS_77!: __VLS_NormalizeEmits<typeof __VLS_76.emit>;
(salle.nomLieu);
(__VLS_76.slots!).default;
}
(__VLS_70.slots!).default;
}
}
(__VLS_54.slots!).default;
}
(__VLS_39.slots!).default;
}
{
const __VLS_78 = ({} as 'VCard' extends keyof typeof __VLS_ctx ? { 'VCard': typeof __VLS_ctx.VCard; } : 'vCard' extends keyof typeof __VLS_ctx ? { 'VCard': typeof __VLS_ctx.vCard; } : 'v-card' extends keyof typeof __VLS_ctx ? { 'VCard': (typeof __VLS_ctx)["v-card"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCard;
const __VLS_79 = __VLS_asFunctionalComponent(__VLS_78, new __VLS_78({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2"), }));
({} as { VCard: typeof __VLS_78; }).VCard;
({} as { VCard: typeof __VLS_78; }).VCard;
const __VLS_80 = __VLS_79({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2"), }, ...__VLS_functionalComponentArgsRest(__VLS_79));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_78, typeof __VLS_80> & Record<string, unknown>) => void)({ ...{}, elevation: ("1"), class: ("rounded-lg pa-2"), });
const __VLS_81 = __VLS_pickFunctionalComponentCtx(__VLS_78, __VLS_80)!;
let __VLS_82!: __VLS_NormalizeEmits<typeof __VLS_81.emit>;
{
const __VLS_83 = ({} as 'VCardTitle' extends keyof typeof __VLS_ctx ? { 'VCardTitle': typeof __VLS_ctx.VCardTitle; } : 'vCardTitle' extends keyof typeof __VLS_ctx ? { 'VCardTitle': typeof __VLS_ctx.vCardTitle; } : 'v-card-title' extends keyof typeof __VLS_ctx ? { 'VCardTitle': (typeof __VLS_ctx)["v-card-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCardTitle;
const __VLS_84 = __VLS_asFunctionalComponent(__VLS_83, new __VLS_83({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), }));
({} as { VCardTitle: typeof __VLS_83; }).VCardTitle;
({} as { VCardTitle: typeof __VLS_83; }).VCardTitle;
const __VLS_85 = __VLS_84({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), }, ...__VLS_functionalComponentArgsRest(__VLS_84));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_83, typeof __VLS_85> & Record<string, unknown>) => void)({ ...{}, class: ("font-weight-bold text-uppercase text-primary"), });
const __VLS_86 = __VLS_pickFunctionalComponentCtx(__VLS_83, __VLS_85)!;
let __VLS_87!: __VLS_NormalizeEmits<typeof __VLS_86.emit>;
(__VLS_86.slots!).default;
}
{
const __VLS_88 = ({} as 'VDivider' extends keyof typeof __VLS_ctx ? { 'VDivider': typeof __VLS_ctx.VDivider; } : 'vDivider' extends keyof typeof __VLS_ctx ? { 'VDivider': typeof __VLS_ctx.vDivider; } : 'v-divider' extends keyof typeof __VLS_ctx ? { 'VDivider': (typeof __VLS_ctx)["v-divider"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VDivider;
const __VLS_89 = __VLS_asFunctionalComponent(__VLS_88, new __VLS_88({ ...{}, }));
({} as { VDivider: typeof __VLS_88; }).VDivider;
({} as { VDivider: typeof __VLS_88; }).VDivider;
const __VLS_90 = __VLS_89({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_89));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_88, typeof __VLS_90> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_91 = __VLS_pickFunctionalComponentCtx(__VLS_88, __VLS_90)!;
let __VLS_92!: __VLS_NormalizeEmits<typeof __VLS_91.emit>;
}
{
const __VLS_93 = ({} as 'VList' extends keyof typeof __VLS_ctx ? { 'VList': typeof __VLS_ctx.VList; } : 'vList' extends keyof typeof __VLS_ctx ? { 'VList': typeof __VLS_ctx.vList; } : 'v-list' extends keyof typeof __VLS_ctx ? { 'VList': (typeof __VLS_ctx)["v-list"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VList;
const __VLS_94 = __VLS_asFunctionalComponent(__VLS_93, new __VLS_93({ ...{}, dense: (true), }));
({} as { VList: typeof __VLS_93; }).VList;
({} as { VList: typeof __VLS_93; }).VList;
const __VLS_95 = __VLS_94({ ...{}, dense: (true), }, ...__VLS_functionalComponentArgsRest(__VLS_94));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_93, typeof __VLS_95> & Record<string, unknown>) => void)({ ...{}, dense: (true), });
const __VLS_96 = __VLS_pickFunctionalComponentCtx(__VLS_93, __VLS_95)!;
let __VLS_97!: __VLS_NormalizeEmits<typeof __VLS_96.emit>;
{
const __VLS_98 = ({} as 'VListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.VListItem; } : 'vListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.vListItem; } : 'v-list-item' extends keyof typeof __VLS_ctx ? { 'VListItem': (typeof __VLS_ctx)["v-list-item"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItem;
const __VLS_99 = __VLS_asFunctionalComponent(__VLS_98, new __VLS_98({ ...{ onClick: {} as any, }, }));
({} as { VListItem: typeof __VLS_98; }).VListItem;
({} as { VListItem: typeof __VLS_98; }).VListItem;
const __VLS_100 = __VLS_99({ ...{ onClick: {} as any, }, }, ...__VLS_functionalComponentArgsRest(__VLS_99));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_98, typeof __VLS_100> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, });
const __VLS_101 = __VLS_pickFunctionalComponentCtx(__VLS_98, __VLS_100)!;
let __VLS_102!: __VLS_NormalizeEmits<typeof __VLS_101.emit>;
let __VLS_103 = { 'click': __VLS_pickEvent(__VLS_102['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_99, typeof __VLS_100>).onClick) };
__VLS_103 = {
click: $event => {
__VLS_ctx.selectTypeEquipement('tous');
// @ts-ignore
[selectTypeEquipement,];
}
};
{
const __VLS_104 = ({} as 'VListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.VListItemTitle; } : 'vListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.vListItemTitle; } : 'v-list-item-title' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': (typeof __VLS_ctx)["v-list-item-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItemTitle;
const __VLS_105 = __VLS_asFunctionalComponent(__VLS_104, new __VLS_104({ ...{}, }));
({} as { VListItemTitle: typeof __VLS_104; }).VListItemTitle;
({} as { VListItemTitle: typeof __VLS_104; }).VListItemTitle;
const __VLS_106 = __VLS_105({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_105));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_104, typeof __VLS_106> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_107 = __VLS_pickFunctionalComponentCtx(__VLS_104, __VLS_106)!;
let __VLS_108!: __VLS_NormalizeEmits<typeof __VLS_107.emit>;
(__VLS_107.slots!).default;
}
(__VLS_101.slots!).default;
}
for (const [type] of __VLS_getVForSourceType((__VLS_ctx.typesEquipements)!)) {
{
const __VLS_109 = ({} as 'VListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.VListItem; } : 'vListItem' extends keyof typeof __VLS_ctx ? { 'VListItem': typeof __VLS_ctx.vListItem; } : 'v-list-item' extends keyof typeof __VLS_ctx ? { 'VListItem': (typeof __VLS_ctx)["v-list-item"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItem;
const __VLS_110 = __VLS_asFunctionalComponent(__VLS_109, new __VLS_109({ ...{ onClick: {} as any, }, key: ((type.id)), }));
({} as { VListItem: typeof __VLS_109; }).VListItem;
({} as { VListItem: typeof __VLS_109; }).VListItem;
const __VLS_111 = __VLS_110({ ...{ onClick: {} as any, }, key: ((type.id)), }, ...__VLS_functionalComponentArgsRest(__VLS_110));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_109, typeof __VLS_111> & Record<string, unknown>) => void)({ ...{ onClick: {} as any, }, key: ((type.id)), });
const __VLS_112 = __VLS_pickFunctionalComponentCtx(__VLS_109, __VLS_111)!;
let __VLS_113!: __VLS_NormalizeEmits<typeof __VLS_112.emit>;
let __VLS_114 = { 'click': __VLS_pickEvent(__VLS_113['click'], ({} as __VLS_FunctionalComponentProps<typeof __VLS_110, typeof __VLS_111>).onClick) };
__VLS_114 = {
click: $event => {
__VLS_ctx.selectTypeEquipement(type.id);
// @ts-ignore
[typesEquipements, selectTypeEquipement,];
}
};
{
const __VLS_115 = ({} as 'VListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.VListItemTitle; } : 'vListItemTitle' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': typeof __VLS_ctx.vListItemTitle; } : 'v-list-item-title' extends keyof typeof __VLS_ctx ? { 'VListItemTitle': (typeof __VLS_ctx)["v-list-item-title"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VListItemTitle;
const __VLS_116 = __VLS_asFunctionalComponent(__VLS_115, new __VLS_115({ ...{}, }));
({} as { VListItemTitle: typeof __VLS_115; }).VListItemTitle;
({} as { VListItemTitle: typeof __VLS_115; }).VListItemTitle;
const __VLS_117 = __VLS_116({ ...{}, }, ...__VLS_functionalComponentArgsRest(__VLS_116));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_115, typeof __VLS_117> & Record<string, unknown>) => void)({ ...{}, });
const __VLS_118 = __VLS_pickFunctionalComponentCtx(__VLS_115, __VLS_117)!;
let __VLS_119!: __VLS_NormalizeEmits<typeof __VLS_118.emit>;
(type.nomModeleEquipement);
(__VLS_118.slots!).default;
}
(__VLS_112.slots!).default;
}
}
(__VLS_96.slots!).default;
}
(__VLS_81.slots!).default;
}
(__VLS_34.slots!).default;
}
{
const __VLS_120 = ({} as 'VCol' extends keyof typeof __VLS_ctx ? { 'VCol': typeof __VLS_ctx.VCol; } : 'vCol' extends keyof typeof __VLS_ctx ? { 'VCol': typeof __VLS_ctx.vCol; } : 'v-col' extends keyof typeof __VLS_ctx ? { 'VCol': (typeof __VLS_ctx)["v-col"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VCol;
const __VLS_121 = __VLS_asFunctionalComponent(__VLS_120, new __VLS_120({ ...{}, cols: ("9"), }));
({} as { VCol: typeof __VLS_120; }).VCol;
({} as { VCol: typeof __VLS_120; }).VCol;
const __VLS_122 = __VLS_121({ ...{}, cols: ("9"), }, ...__VLS_functionalComponentArgsRest(__VLS_121));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_120, typeof __VLS_122> & Record<string, unknown>) => void)({ ...{}, cols: ("9"), });
const __VLS_123 = __VLS_pickFunctionalComponentCtx(__VLS_120, __VLS_122)!;
let __VLS_124!: __VLS_NormalizeEmits<typeof __VLS_123.emit>;
{
const __VLS_125 = ({} as 'VDataTable' extends keyof typeof __VLS_ctx ? { 'VDataTable': typeof __VLS_ctx.VDataTable; } : 'vDataTable' extends keyof typeof __VLS_ctx ? { 'VDataTable': typeof __VLS_ctx.vDataTable; } : 'v-data-table' extends keyof typeof __VLS_ctx ? { 'VDataTable': (typeof __VLS_ctx)["v-data-table"]; } : typeof __VLS_resolvedLocalAndGlobalComponents).VDataTable;
const __VLS_126 = __VLS_asFunctionalComponent(__VLS_125, new __VLS_125({ ...{}, headers: ((__VLS_ctx.headers)), items: ((__VLS_ctx.equipements)), itemValue: ("name"), class: ("elevation-1 rounded-lg"), hideDefaultFooter: (true), }));
({} as { VDataTable: typeof __VLS_125; }).VDataTable;
({} as { VDataTable: typeof __VLS_125; }).VDataTable;
const __VLS_127 = __VLS_126({ ...{}, headers: ((__VLS_ctx.headers)), items: ((__VLS_ctx.equipements)), itemValue: ("name"), class: ("elevation-1 rounded-lg"), hideDefaultFooter: (true), }, ...__VLS_functionalComponentArgsRest(__VLS_126));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_125, typeof __VLS_127> & Record<string, unknown>) => void)({ ...{}, headers: ((__VLS_ctx.headers)), items: ((__VLS_ctx.equipements)), itemValue: ("name"), class: ("elevation-1 rounded-lg"), hideDefaultFooter: (true), });
const __VLS_128 = __VLS_pickFunctionalComponentCtx(__VLS_125, __VLS_127)!;
let __VLS_129!: __VLS_NormalizeEmits<typeof __VLS_128.emit>;
}
(__VLS_123.slots!).default;
}
(__VLS_29.slots!).default;
}
(__VLS_24.slots!).default;
}
(__VLS_19.slots!).default;
}
(__VLS_3.slots!).default;
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
}
var __VLS_slots!: {};
// @ts-ignore
[headers, equipements, headers, equipements, headers, equipements,];
return __VLS_slots;
}
