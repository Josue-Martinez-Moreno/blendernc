import bpy
import os


gui_active_panel_fin = None

class ButtonLoadOn(bpy.types.Operator):
    bl_label = 'Load netCDF'
    bl_idname = 'blendernc.button_file_on'
    bl_description = 'Open file and netCDF panel'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        global gui_active_panel_fin
        gui_active_panel_fin = "Files"
        return {'FINISHED'}


class ButtonLoadOff(bpy.types.Operator):
    bl_label = 'Load netCDF'
    bl_idname = 'blendernc.button_file_off'
    bl_description = 'Close file and netCDF panel'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        global gui_active_panel_fin
        gui_active_panel_fin = None
        return {'FINISHED'}

class Blendernc_Panel(bpy.types.Panel):
    bl_idname = "BLENDERNC_PT_Panel"
    bl_label = "Blendernc"
    bl_category = "Blendernc"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self,context):
        icon_expand = "DISCLOSURE_TRI_RIGHT"
        icon_collapse = "DISCLOSURE_TRI_DOWN"

        box_post_opt = self.layout.box()
        scn=context.scene

        box_post_opt.label(text="Load netCDF", icon='MODIFIER_ON')

        if gui_active_panel_fin != "Files":
            box_post_opt.operator('blendernc.button_file_on', icon=icon_expand)
        else:
            box_post_opt.operator('blendernc.button_file_off', icon=icon_collapse)
            # assets_status = mblab_proxy.validate_assets_fitting()
            box_asts = box_post_opt.box()

            #Open folders
            box_asts.label(text="netCDF File", icon='OUTLINER_OB_GROUP_INSTANCE')
            box_asts.prop(scn, 'blendernc_file')

            box_asts.operator('blendernc.netcdf_load', text="Load netCDF")
            #box_asts.prop(scn, 'mblab_assets_models')
            # box.operator('mbast.load_assets_element')
            box_asts.label(text="Select variable:", icon='WORLD_DATA')
            box_asts.prop(scn, 'blendernc_netcdf_vars')

            box_asts.label(text="INFO", icon='INFO')

        #row.operator('view3d.open_file', text="Center 3D Cursor")
        #row.prop(scn.load_file,'get_path', text='Dataset Path',icon='FILESEL')

        box_post_opt.operator('blendernc.cursor_center', text="Center 3D Cursor")







