'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_direct_state_access'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_direct_state_access',error_checker=_errors._error_checker)
GL_QUERY_TARGET=_C('GL_QUERY_TARGET',0x82EA)
GL_TEXTURE_BINDING_1D=_C('GL_TEXTURE_BINDING_1D',0x8068)
GL_TEXTURE_BINDING_1D_ARRAY=_C('GL_TEXTURE_BINDING_1D_ARRAY',0x8C1C)
GL_TEXTURE_BINDING_2D=_C('GL_TEXTURE_BINDING_2D',0x8069)
GL_TEXTURE_BINDING_2D_ARRAY=_C('GL_TEXTURE_BINDING_2D_ARRAY',0x8C1D)
GL_TEXTURE_BINDING_2D_MULTISAMPLE=_C('GL_TEXTURE_BINDING_2D_MULTISAMPLE',0x9104)
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY=_C('GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY',0x9105)
GL_TEXTURE_BINDING_3D=_C('GL_TEXTURE_BINDING_3D',0x806A)
GL_TEXTURE_BINDING_BUFFER=_C('GL_TEXTURE_BINDING_BUFFER',0x8C2C)
GL_TEXTURE_BINDING_CUBE_MAP=_C('GL_TEXTURE_BINDING_CUBE_MAP',0x8514)
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY=_C('GL_TEXTURE_BINDING_CUBE_MAP_ARRAY',0x900A)
GL_TEXTURE_BINDING_RECTANGLE=_C('GL_TEXTURE_BINDING_RECTANGLE',0x84F6)
GL_TEXTURE_TARGET=_C('GL_TEXTURE_TARGET',0x1006)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glBindTextureUnit(unit,texture):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitNamedFramebuffer(readFramebuffer,drawFramebuffer,srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter):pass
@_f
@_p.types(_cs.GLenum,_cs.GLuint,_cs.GLenum)
def glCheckNamedFramebufferStatus(framebuffer,target):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glClearNamedBufferData(buffer,internalformat,format,type,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glClearNamedBufferSubData(buffer,internalformat,offset,size,format,type,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLfloat,_cs.GLint)
def glClearNamedFramebufferfi(framebuffer,buffer,drawbuffer,depth,stencil):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glClearNamedFramebufferfv(framebuffer,buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,arrays.GLintArray)
def glClearNamedFramebufferiv(framebuffer,buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,arrays.GLuintArray)
def glClearNamedFramebufferuiv(framebuffer,buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage1D(texture,level,xoffset,width,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage2D(texture,level,xoffset,yoffset,width,height,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage3D(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glCopyNamedBufferSubData(readBuffer,writeBuffer,readOffset,writeOffset,size):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyTextureSubImage1D(texture,level,xoffset,x,y,width):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTextureSubImage2D(texture,level,xoffset,yoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTextureSubImage3D(texture,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateFramebuffers(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateProgramPipelines(n,pipelines):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glCreateQueries(target,n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateRenderbuffers(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateSamplers(n,samplers):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glCreateTextures(target,n,textures):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateVertexArrays(n,arrays):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glDisableVertexArrayAttrib(vaobj,index):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glEnableVertexArrayAttrib(vaobj,index):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedNamedBufferRange(buffer,offset,length):pass
@_f
@_p.types(None,_cs.GLuint)
def glGenerateTextureMipmap(texture):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glGetCompressedTextureImage(texture,level,bufSize,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetNamedBufferParameteri64v(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedBufferParameteriv(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLvoidpArray)
def glGetNamedBufferPointerv(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glGetNamedBufferSubData(buffer,offset,size,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetNamedFramebufferAttachmentParameteriv(framebuffer,attachment,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedFramebufferParameteriv(framebuffer,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedRenderbufferParameteriv(renderbuffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLintptr)
def glGetQueryBufferObjecti64v(id,buffer,pname,offset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLintptr)
def glGetQueryBufferObjectiv(id,buffer,pname,offset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLintptr)
def glGetQueryBufferObjectui64v(id,buffer,pname,offset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLintptr)
def glGetQueryBufferObjectuiv(id,buffer,pname,offset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glGetTextureImage(texture,level,format,type,bufSize,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,arrays.GLfloatArray)
def glGetTextureLevelParameterfv(texture,level,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,arrays.GLintArray)
def glGetTextureLevelParameteriv(texture,level,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetTextureParameterIiv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetTextureParameterIuiv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetTextureParameterfv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetTextureParameteriv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLint64Array)
def glGetTransformFeedbacki64_v(xfb,pname,index,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetTransformFeedbacki_v(xfb,pname,index,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetTransformFeedbackiv(xfb,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetVertexArrayIndexed64iv(vaobj,index,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexArrayIndexediv(vaobj,index,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexArrayiv(vaobj,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glInvalidateNamedFramebufferData(framebuffer,numAttachments,attachments):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glInvalidateNamedFramebufferSubData(framebuffer,numAttachments,attachments,x,y,width,height):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLuint,_cs.GLenum)
def glMapNamedBuffer(buffer,access):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLbitfield)
def glMapNamedBufferRange(buffer,offset,length,access):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLenum)
def glNamedBufferData(buffer,size,data,usage):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLbitfield)
def glNamedBufferStorage(buffer,size,data,flags):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glNamedBufferSubData(buffer,offset,size,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glNamedFramebufferDrawBuffer(framebuffer,buf):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glNamedFramebufferDrawBuffers(framebuffer,n,bufs):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glNamedFramebufferParameteri(framebuffer,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glNamedFramebufferReadBuffer(framebuffer,src):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glNamedFramebufferRenderbuffer(framebuffer,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glNamedFramebufferTexture(framebuffer,attachment,texture,level):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glNamedFramebufferTextureLayer(framebuffer,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorage(renderbuffer,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorageMultisample(renderbuffer,samples,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glTextureBuffer(texture,internalformat,buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glTextureBufferRange(texture,internalformat,buffer,offset,size):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glTextureParameterIiv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glTextureParameterIuiv(texture,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLfloat)
def glTextureParameterf(texture,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glTextureParameterfv(texture,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glTextureParameteri(texture,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glTextureParameteriv(texture,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei)
def glTextureStorage1D(texture,levels,internalformat,width):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTextureStorage2D(texture,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureStorage2DMultisample(texture,samples,internalformat,width,height,fixedsamplelocations):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glTextureStorage3D(texture,levels,internalformat,width,height,depth):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureStorage3DMultisample(texture,samples,internalformat,width,height,depth,fixedsamplelocations):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage1D(texture,level,xoffset,width,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage2D(texture,level,xoffset,yoffset,width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage3D(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glTransformFeedbackBufferBase(xfb,index,buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glTransformFeedbackBufferRange(xfb,index,buffer,offset,size):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glUnmapNamedBuffer(buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexArrayAttribBinding(vaobj,attribindex,bindingindex):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexArrayAttribFormat(vaobj,attribindex,size,type,normalized,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLuint)
def glVertexArrayAttribIFormat(vaobj,attribindex,size,type,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLuint)
def glVertexArrayAttribLFormat(vaobj,attribindex,size,type,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexArrayBindingDivisor(vaobj,bindingindex,divisor):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexArrayElementBuffer(vaobj,buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizei)
def glVertexArrayVertexBuffer(vaobj,bindingindex,buffer,offset,stride):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,ctypes.POINTER(_cs.GLintptr),arrays.GLsizeiArray)
def glVertexArrayVertexBuffers(vaobj,first,count,buffers,offsets,strides):pass
