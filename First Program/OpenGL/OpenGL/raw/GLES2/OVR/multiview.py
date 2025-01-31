'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_OVR_multiview'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_OVR_multiview',error_checker=_errors._error_checker)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR',0x9632)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR',0x9630)
GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR=_C('GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR',0x9633)
GL_MAX_VIEWS_OVR=_C('GL_MAX_VIEWS_OVR',0x9631)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glFramebufferTextureMultiviewOVR(target,attachment,texture,level,baseViewIndex,numViews):pass
