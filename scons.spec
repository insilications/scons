#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scons
Version  : 3.0.1
Release  : 18
URL      : https://prdownloads.sourceforge.net/scons/scons-3.0.1.tar.gz
Source0  : https://prdownloads.sourceforge.net/scons/scons-3.0.1.tar.gz
Summary  : Open Source next-generation build tool.
Group    : Development/Tools
License  : MIT
Requires: scons-bin
Requires: scons-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: manpage.patch

%description
Improved, cross-platform substitute for the classic Make
        utility.  In short, SCons is an easier, more reliable
        and faster way to build software.

%package bin
Summary: bin components for the scons package.
Group: Binaries

%description bin
bin components for the scons package.


%package doc
Summary: doc components for the scons package.
Group: Documentation

%description doc
doc components for the scons package.


%prep
%setup -q -n scons-3.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524857340
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/scons-3.0.1/SCons/Action.py
/usr/lib/scons-3.0.1/SCons/Action.pyc
/usr/lib/scons-3.0.1/SCons/Builder.py
/usr/lib/scons-3.0.1/SCons/Builder.pyc
/usr/lib/scons-3.0.1/SCons/CacheDir.py
/usr/lib/scons-3.0.1/SCons/CacheDir.pyc
/usr/lib/scons-3.0.1/SCons/Conftest.py
/usr/lib/scons-3.0.1/SCons/Conftest.pyc
/usr/lib/scons-3.0.1/SCons/Debug.py
/usr/lib/scons-3.0.1/SCons/Debug.pyc
/usr/lib/scons-3.0.1/SCons/Defaults.py
/usr/lib/scons-3.0.1/SCons/Defaults.pyc
/usr/lib/scons-3.0.1/SCons/Environment.py
/usr/lib/scons-3.0.1/SCons/Environment.pyc
/usr/lib/scons-3.0.1/SCons/Errors.py
/usr/lib/scons-3.0.1/SCons/Errors.pyc
/usr/lib/scons-3.0.1/SCons/Executor.py
/usr/lib/scons-3.0.1/SCons/Executor.pyc
/usr/lib/scons-3.0.1/SCons/Job.py
/usr/lib/scons-3.0.1/SCons/Job.pyc
/usr/lib/scons-3.0.1/SCons/Memoize.py
/usr/lib/scons-3.0.1/SCons/Memoize.pyc
/usr/lib/scons-3.0.1/SCons/Node/Alias.py
/usr/lib/scons-3.0.1/SCons/Node/Alias.pyc
/usr/lib/scons-3.0.1/SCons/Node/FS.py
/usr/lib/scons-3.0.1/SCons/Node/FS.pyc
/usr/lib/scons-3.0.1/SCons/Node/Python.py
/usr/lib/scons-3.0.1/SCons/Node/Python.pyc
/usr/lib/scons-3.0.1/SCons/Node/__init__.py
/usr/lib/scons-3.0.1/SCons/Node/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Node/__pycache__/Alias.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Node/__pycache__/FS.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Node/__pycache__/Python.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Node/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/BoolOption.py
/usr/lib/scons-3.0.1/SCons/Options/BoolOption.pyc
/usr/lib/scons-3.0.1/SCons/Options/EnumOption.py
/usr/lib/scons-3.0.1/SCons/Options/EnumOption.pyc
/usr/lib/scons-3.0.1/SCons/Options/ListOption.py
/usr/lib/scons-3.0.1/SCons/Options/ListOption.pyc
/usr/lib/scons-3.0.1/SCons/Options/PackageOption.py
/usr/lib/scons-3.0.1/SCons/Options/PackageOption.pyc
/usr/lib/scons-3.0.1/SCons/Options/PathOption.py
/usr/lib/scons-3.0.1/SCons/Options/PathOption.pyc
/usr/lib/scons-3.0.1/SCons/Options/__init__.py
/usr/lib/scons-3.0.1/SCons/Options/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/BoolOption.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/EnumOption.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/ListOption.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/PackageOption.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/PathOption.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Options/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/PathList.py
/usr/lib/scons-3.0.1/SCons/PathList.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__init__.py
/usr/lib/scons-3.0.1/SCons/Platform/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/aix.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/cygwin.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/darwin.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/hpux.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/irix.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/os2.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/posix.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/sunos.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/__pycache__/win32.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Platform/aix.py
/usr/lib/scons-3.0.1/SCons/Platform/aix.pyc
/usr/lib/scons-3.0.1/SCons/Platform/cygwin.py
/usr/lib/scons-3.0.1/SCons/Platform/cygwin.pyc
/usr/lib/scons-3.0.1/SCons/Platform/darwin.py
/usr/lib/scons-3.0.1/SCons/Platform/darwin.pyc
/usr/lib/scons-3.0.1/SCons/Platform/hpux.py
/usr/lib/scons-3.0.1/SCons/Platform/hpux.pyc
/usr/lib/scons-3.0.1/SCons/Platform/irix.py
/usr/lib/scons-3.0.1/SCons/Platform/irix.pyc
/usr/lib/scons-3.0.1/SCons/Platform/os2.py
/usr/lib/scons-3.0.1/SCons/Platform/os2.pyc
/usr/lib/scons-3.0.1/SCons/Platform/posix.py
/usr/lib/scons-3.0.1/SCons/Platform/posix.pyc
/usr/lib/scons-3.0.1/SCons/Platform/sunos.py
/usr/lib/scons-3.0.1/SCons/Platform/sunos.pyc
/usr/lib/scons-3.0.1/SCons/Platform/win32.py
/usr/lib/scons-3.0.1/SCons/Platform/win32.pyc
/usr/lib/scons-3.0.1/SCons/SConf.py
/usr/lib/scons-3.0.1/SCons/SConf.pyc
/usr/lib/scons-3.0.1/SCons/SConsign.py
/usr/lib/scons-3.0.1/SCons/SConsign.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/C.py
/usr/lib/scons-3.0.1/SCons/Scanner/C.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/D.py
/usr/lib/scons-3.0.1/SCons/Scanner/D.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/Dir.py
/usr/lib/scons-3.0.1/SCons/Scanner/Dir.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/Fortran.py
/usr/lib/scons-3.0.1/SCons/Scanner/Fortran.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/IDL.py
/usr/lib/scons-3.0.1/SCons/Scanner/IDL.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/LaTeX.py
/usr/lib/scons-3.0.1/SCons/Scanner/LaTeX.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/Prog.py
/usr/lib/scons-3.0.1/SCons/Scanner/Prog.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/RC.py
/usr/lib/scons-3.0.1/SCons/Scanner/RC.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/SWIG.py
/usr/lib/scons-3.0.1/SCons/Scanner/SWIG.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__init__.py
/usr/lib/scons-3.0.1/SCons/Scanner/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/C.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/D.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/Dir.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/Fortran.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/IDL.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/LaTeX.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/Prog.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/RC.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/SWIG.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Scanner/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Script/Interactive.py
/usr/lib/scons-3.0.1/SCons/Script/Interactive.pyc
/usr/lib/scons-3.0.1/SCons/Script/Main.py
/usr/lib/scons-3.0.1/SCons/Script/Main.pyc
/usr/lib/scons-3.0.1/SCons/Script/SConsOptions.py
/usr/lib/scons-3.0.1/SCons/Script/SConsOptions.pyc
/usr/lib/scons-3.0.1/SCons/Script/SConscript.py
/usr/lib/scons-3.0.1/SCons/Script/SConscript.pyc
/usr/lib/scons-3.0.1/SCons/Script/__init__.py
/usr/lib/scons-3.0.1/SCons/Script/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Script/__pycache__/Interactive.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Script/__pycache__/Main.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Script/__pycache__/SConsOptions.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Script/__pycache__/SConscript.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Script/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Subst.py
/usr/lib/scons-3.0.1/SCons/Subst.pyc
/usr/lib/scons-3.0.1/SCons/Taskmaster.py
/usr/lib/scons-3.0.1/SCons/Taskmaster.pyc
/usr/lib/scons-3.0.1/SCons/Tool/386asm.py
/usr/lib/scons-3.0.1/SCons/Tool/386asm.pyc
/usr/lib/scons-3.0.1/SCons/Tool/DCommon.py
/usr/lib/scons-3.0.1/SCons/Tool/DCommon.pyc
/usr/lib/scons-3.0.1/SCons/Tool/FortranCommon.py
/usr/lib/scons-3.0.1/SCons/Tool/FortranCommon.pyc
/usr/lib/scons-3.0.1/SCons/Tool/GettextCommon.py
/usr/lib/scons-3.0.1/SCons/Tool/GettextCommon.pyc
/usr/lib/scons-3.0.1/SCons/Tool/JavaCommon.py
/usr/lib/scons-3.0.1/SCons/Tool/JavaCommon.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__init__.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/arch.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/common.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/netframework.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/sdk.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/vc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/__pycache__/vs.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/arch.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/arch.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/common.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/common.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/netframework.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/netframework.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/sdk.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/sdk.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/vc.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/vc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/vs.py
/usr/lib/scons-3.0.1/SCons/Tool/MSCommon/vs.pyc
/usr/lib/scons-3.0.1/SCons/Tool/PharLapCommon.py
/usr/lib/scons-3.0.1/SCons/Tool/PharLapCommon.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__init__.py
/usr/lib/scons-3.0.1/SCons/Tool/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/386asm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/DCommon.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/FortranCommon.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/GettextCommon.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/JavaCommon.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/PharLapCommon.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/aixc++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/aixcc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/aixcxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/aixf77.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/aixlink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/applelink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ar.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/as.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/bcc32.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/c++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/cc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/clang.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/clangxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/cvf.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/cxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/cyglink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/default.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/dmd.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/dvi.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/dvipdf.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/dvips.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/f03.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/f08.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/f77.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/f90.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/f95.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/filesystem.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/fortran.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/g++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/g77.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gas.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gcc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gdc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gettext_tool.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gfortran.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gnulink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gs.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/gxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/hpc++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/hpcc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/hpcxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/hplink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/icc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/icl.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ifl.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ifort.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ilink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ilink32.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/install.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/intelc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ipkg.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/jar.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/javac.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/javah.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/latex.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/ldc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/lex.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/link.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/linkloc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/m4.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/masm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/midl.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mingw.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/msgfmt.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/msginit.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/msgmerge.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mslib.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mslink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mssdk.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/msvc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/msvs.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mwcc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/mwld.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/nasm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/pdf.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/pdflatex.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/pdftex.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/qt.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/rmic.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/rpcgen.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/rpm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/rpmutils.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sgiar.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sgic++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sgicc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sgicxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sgilink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunar.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunc++.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/suncc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/suncxx.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunf77.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunf90.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunf95.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/sunlink.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/swig.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/tar.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/tex.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/textfile.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/tlib.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/wix.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/xgettext.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/yacc.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/__pycache__/zip.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/aixc++.py
/usr/lib/scons-3.0.1/SCons/Tool/aixc++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/aixcc.py
/usr/lib/scons-3.0.1/SCons/Tool/aixcc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/aixcxx.py
/usr/lib/scons-3.0.1/SCons/Tool/aixcxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/aixf77.py
/usr/lib/scons-3.0.1/SCons/Tool/aixf77.pyc
/usr/lib/scons-3.0.1/SCons/Tool/aixlink.py
/usr/lib/scons-3.0.1/SCons/Tool/aixlink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/applelink.py
/usr/lib/scons-3.0.1/SCons/Tool/applelink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ar.py
/usr/lib/scons-3.0.1/SCons/Tool/ar.pyc
/usr/lib/scons-3.0.1/SCons/Tool/as.py
/usr/lib/scons-3.0.1/SCons/Tool/as.pyc
/usr/lib/scons-3.0.1/SCons/Tool/bcc32.py
/usr/lib/scons-3.0.1/SCons/Tool/bcc32.pyc
/usr/lib/scons-3.0.1/SCons/Tool/c++.py
/usr/lib/scons-3.0.1/SCons/Tool/c++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/cc.py
/usr/lib/scons-3.0.1/SCons/Tool/cc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/clang.py
/usr/lib/scons-3.0.1/SCons/Tool/clang.pyc
/usr/lib/scons-3.0.1/SCons/Tool/clangxx.py
/usr/lib/scons-3.0.1/SCons/Tool/clangxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/cvf.py
/usr/lib/scons-3.0.1/SCons/Tool/cvf.pyc
/usr/lib/scons-3.0.1/SCons/Tool/cxx.py
/usr/lib/scons-3.0.1/SCons/Tool/cxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/cyglink.py
/usr/lib/scons-3.0.1/SCons/Tool/cyglink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/default.py
/usr/lib/scons-3.0.1/SCons/Tool/default.pyc
/usr/lib/scons-3.0.1/SCons/Tool/dmd.py
/usr/lib/scons-3.0.1/SCons/Tool/dmd.pyc
/usr/lib/scons-3.0.1/SCons/Tool/docbook/__init__.py
/usr/lib/scons-3.0.1/SCons/Tool/docbook/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Tool/docbook/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/dvi.py
/usr/lib/scons-3.0.1/SCons/Tool/dvi.pyc
/usr/lib/scons-3.0.1/SCons/Tool/dvipdf.py
/usr/lib/scons-3.0.1/SCons/Tool/dvipdf.pyc
/usr/lib/scons-3.0.1/SCons/Tool/dvips.py
/usr/lib/scons-3.0.1/SCons/Tool/dvips.pyc
/usr/lib/scons-3.0.1/SCons/Tool/f03.py
/usr/lib/scons-3.0.1/SCons/Tool/f03.pyc
/usr/lib/scons-3.0.1/SCons/Tool/f08.py
/usr/lib/scons-3.0.1/SCons/Tool/f08.pyc
/usr/lib/scons-3.0.1/SCons/Tool/f77.py
/usr/lib/scons-3.0.1/SCons/Tool/f77.pyc
/usr/lib/scons-3.0.1/SCons/Tool/f90.py
/usr/lib/scons-3.0.1/SCons/Tool/f90.pyc
/usr/lib/scons-3.0.1/SCons/Tool/f95.py
/usr/lib/scons-3.0.1/SCons/Tool/f95.pyc
/usr/lib/scons-3.0.1/SCons/Tool/filesystem.py
/usr/lib/scons-3.0.1/SCons/Tool/filesystem.pyc
/usr/lib/scons-3.0.1/SCons/Tool/fortran.py
/usr/lib/scons-3.0.1/SCons/Tool/fortran.pyc
/usr/lib/scons-3.0.1/SCons/Tool/g++.py
/usr/lib/scons-3.0.1/SCons/Tool/g++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/g77.py
/usr/lib/scons-3.0.1/SCons/Tool/g77.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gas.py
/usr/lib/scons-3.0.1/SCons/Tool/gas.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gcc.py
/usr/lib/scons-3.0.1/SCons/Tool/gcc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gdc.py
/usr/lib/scons-3.0.1/SCons/Tool/gdc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gettext_tool.py
/usr/lib/scons-3.0.1/SCons/Tool/gettext_tool.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gfortran.py
/usr/lib/scons-3.0.1/SCons/Tool/gfortran.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gnulink.py
/usr/lib/scons-3.0.1/SCons/Tool/gnulink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gs.py
/usr/lib/scons-3.0.1/SCons/Tool/gs.pyc
/usr/lib/scons-3.0.1/SCons/Tool/gxx.py
/usr/lib/scons-3.0.1/SCons/Tool/gxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/hpc++.py
/usr/lib/scons-3.0.1/SCons/Tool/hpc++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/hpcc.py
/usr/lib/scons-3.0.1/SCons/Tool/hpcc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/hpcxx.py
/usr/lib/scons-3.0.1/SCons/Tool/hpcxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/hplink.py
/usr/lib/scons-3.0.1/SCons/Tool/hplink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/icc.py
/usr/lib/scons-3.0.1/SCons/Tool/icc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/icl.py
/usr/lib/scons-3.0.1/SCons/Tool/icl.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ifl.py
/usr/lib/scons-3.0.1/SCons/Tool/ifl.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ifort.py
/usr/lib/scons-3.0.1/SCons/Tool/ifort.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ilink.py
/usr/lib/scons-3.0.1/SCons/Tool/ilink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ilink32.py
/usr/lib/scons-3.0.1/SCons/Tool/ilink32.pyc
/usr/lib/scons-3.0.1/SCons/Tool/install.py
/usr/lib/scons-3.0.1/SCons/Tool/install.pyc
/usr/lib/scons-3.0.1/SCons/Tool/intelc.py
/usr/lib/scons-3.0.1/SCons/Tool/intelc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ipkg.py
/usr/lib/scons-3.0.1/SCons/Tool/ipkg.pyc
/usr/lib/scons-3.0.1/SCons/Tool/jar.py
/usr/lib/scons-3.0.1/SCons/Tool/jar.pyc
/usr/lib/scons-3.0.1/SCons/Tool/javac.py
/usr/lib/scons-3.0.1/SCons/Tool/javac.pyc
/usr/lib/scons-3.0.1/SCons/Tool/javah.py
/usr/lib/scons-3.0.1/SCons/Tool/javah.pyc
/usr/lib/scons-3.0.1/SCons/Tool/latex.py
/usr/lib/scons-3.0.1/SCons/Tool/latex.pyc
/usr/lib/scons-3.0.1/SCons/Tool/ldc.py
/usr/lib/scons-3.0.1/SCons/Tool/ldc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/lex.py
/usr/lib/scons-3.0.1/SCons/Tool/lex.pyc
/usr/lib/scons-3.0.1/SCons/Tool/link.py
/usr/lib/scons-3.0.1/SCons/Tool/link.pyc
/usr/lib/scons-3.0.1/SCons/Tool/linkloc.py
/usr/lib/scons-3.0.1/SCons/Tool/linkloc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/m4.py
/usr/lib/scons-3.0.1/SCons/Tool/m4.pyc
/usr/lib/scons-3.0.1/SCons/Tool/masm.py
/usr/lib/scons-3.0.1/SCons/Tool/masm.pyc
/usr/lib/scons-3.0.1/SCons/Tool/midl.py
/usr/lib/scons-3.0.1/SCons/Tool/midl.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mingw.py
/usr/lib/scons-3.0.1/SCons/Tool/mingw.pyc
/usr/lib/scons-3.0.1/SCons/Tool/msgfmt.py
/usr/lib/scons-3.0.1/SCons/Tool/msgfmt.pyc
/usr/lib/scons-3.0.1/SCons/Tool/msginit.py
/usr/lib/scons-3.0.1/SCons/Tool/msginit.pyc
/usr/lib/scons-3.0.1/SCons/Tool/msgmerge.py
/usr/lib/scons-3.0.1/SCons/Tool/msgmerge.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mslib.py
/usr/lib/scons-3.0.1/SCons/Tool/mslib.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mslink.py
/usr/lib/scons-3.0.1/SCons/Tool/mslink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mssdk.py
/usr/lib/scons-3.0.1/SCons/Tool/mssdk.pyc
/usr/lib/scons-3.0.1/SCons/Tool/msvc.py
/usr/lib/scons-3.0.1/SCons/Tool/msvc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/msvs.py
/usr/lib/scons-3.0.1/SCons/Tool/msvs.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mwcc.py
/usr/lib/scons-3.0.1/SCons/Tool/mwcc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/mwld.py
/usr/lib/scons-3.0.1/SCons/Tool/mwld.pyc
/usr/lib/scons-3.0.1/SCons/Tool/nasm.py
/usr/lib/scons-3.0.1/SCons/Tool/nasm.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__init__.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/ipk.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/msi.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/rpm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/src_tarbz2.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/src_targz.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/src_zip.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/tarbz2.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/targz.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/__pycache__/zip.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/ipk.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/ipk.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/msi.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/msi.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/rpm.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/rpm.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_tarbz2.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_tarbz2.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_targz.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_targz.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_zip.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/src_zip.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/tarbz2.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/tarbz2.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/targz.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/targz.pyc
/usr/lib/scons-3.0.1/SCons/Tool/packaging/zip.py
/usr/lib/scons-3.0.1/SCons/Tool/packaging/zip.pyc
/usr/lib/scons-3.0.1/SCons/Tool/pdf.py
/usr/lib/scons-3.0.1/SCons/Tool/pdf.pyc
/usr/lib/scons-3.0.1/SCons/Tool/pdflatex.py
/usr/lib/scons-3.0.1/SCons/Tool/pdflatex.pyc
/usr/lib/scons-3.0.1/SCons/Tool/pdftex.py
/usr/lib/scons-3.0.1/SCons/Tool/pdftex.pyc
/usr/lib/scons-3.0.1/SCons/Tool/qt.py
/usr/lib/scons-3.0.1/SCons/Tool/qt.pyc
/usr/lib/scons-3.0.1/SCons/Tool/rmic.py
/usr/lib/scons-3.0.1/SCons/Tool/rmic.pyc
/usr/lib/scons-3.0.1/SCons/Tool/rpcgen.py
/usr/lib/scons-3.0.1/SCons/Tool/rpcgen.pyc
/usr/lib/scons-3.0.1/SCons/Tool/rpm.py
/usr/lib/scons-3.0.1/SCons/Tool/rpm.pyc
/usr/lib/scons-3.0.1/SCons/Tool/rpmutils.py
/usr/lib/scons-3.0.1/SCons/Tool/rpmutils.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sgiar.py
/usr/lib/scons-3.0.1/SCons/Tool/sgiar.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sgic++.py
/usr/lib/scons-3.0.1/SCons/Tool/sgic++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sgicc.py
/usr/lib/scons-3.0.1/SCons/Tool/sgicc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sgicxx.py
/usr/lib/scons-3.0.1/SCons/Tool/sgicxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sgilink.py
/usr/lib/scons-3.0.1/SCons/Tool/sgilink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunar.py
/usr/lib/scons-3.0.1/SCons/Tool/sunar.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunc++.py
/usr/lib/scons-3.0.1/SCons/Tool/sunc++.pyc
/usr/lib/scons-3.0.1/SCons/Tool/suncc.py
/usr/lib/scons-3.0.1/SCons/Tool/suncc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/suncxx.py
/usr/lib/scons-3.0.1/SCons/Tool/suncxx.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunf77.py
/usr/lib/scons-3.0.1/SCons/Tool/sunf77.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunf90.py
/usr/lib/scons-3.0.1/SCons/Tool/sunf90.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunf95.py
/usr/lib/scons-3.0.1/SCons/Tool/sunf95.pyc
/usr/lib/scons-3.0.1/SCons/Tool/sunlink.py
/usr/lib/scons-3.0.1/SCons/Tool/sunlink.pyc
/usr/lib/scons-3.0.1/SCons/Tool/swig.py
/usr/lib/scons-3.0.1/SCons/Tool/swig.pyc
/usr/lib/scons-3.0.1/SCons/Tool/tar.py
/usr/lib/scons-3.0.1/SCons/Tool/tar.pyc
/usr/lib/scons-3.0.1/SCons/Tool/tex.py
/usr/lib/scons-3.0.1/SCons/Tool/tex.pyc
/usr/lib/scons-3.0.1/SCons/Tool/textfile.py
/usr/lib/scons-3.0.1/SCons/Tool/textfile.pyc
/usr/lib/scons-3.0.1/SCons/Tool/tlib.py
/usr/lib/scons-3.0.1/SCons/Tool/tlib.pyc
/usr/lib/scons-3.0.1/SCons/Tool/wix.py
/usr/lib/scons-3.0.1/SCons/Tool/wix.pyc
/usr/lib/scons-3.0.1/SCons/Tool/xgettext.py
/usr/lib/scons-3.0.1/SCons/Tool/xgettext.pyc
/usr/lib/scons-3.0.1/SCons/Tool/yacc.py
/usr/lib/scons-3.0.1/SCons/Tool/yacc.pyc
/usr/lib/scons-3.0.1/SCons/Tool/zip.py
/usr/lib/scons-3.0.1/SCons/Tool/zip.pyc
/usr/lib/scons-3.0.1/SCons/Util.py
/usr/lib/scons-3.0.1/SCons/Util.pyc
/usr/lib/scons-3.0.1/SCons/Variables/BoolVariable.py
/usr/lib/scons-3.0.1/SCons/Variables/BoolVariable.pyc
/usr/lib/scons-3.0.1/SCons/Variables/EnumVariable.py
/usr/lib/scons-3.0.1/SCons/Variables/EnumVariable.pyc
/usr/lib/scons-3.0.1/SCons/Variables/ListVariable.py
/usr/lib/scons-3.0.1/SCons/Variables/ListVariable.pyc
/usr/lib/scons-3.0.1/SCons/Variables/PackageVariable.py
/usr/lib/scons-3.0.1/SCons/Variables/PackageVariable.pyc
/usr/lib/scons-3.0.1/SCons/Variables/PathVariable.py
/usr/lib/scons-3.0.1/SCons/Variables/PathVariable.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__init__.py
/usr/lib/scons-3.0.1/SCons/Variables/__init__.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/BoolVariable.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/EnumVariable.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/ListVariable.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/PackageVariable.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/PathVariable.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Variables/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/Warnings.py
/usr/lib/scons-3.0.1/SCons/Warnings.pyc
/usr/lib/scons-3.0.1/SCons/__init__.py
/usr/lib/scons-3.0.1/SCons/__init__.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Action.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Builder.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/CacheDir.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Conftest.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Debug.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Defaults.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Environment.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Errors.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Executor.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Job.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Memoize.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/PathList.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/SConf.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/SConsign.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Subst.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Taskmaster.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Util.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/Warnings.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/cpp.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/dblite.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/__pycache__/exitfuncs.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/compat/__init__.py
/usr/lib/scons-3.0.1/SCons/compat/__init__.pyc
/usr/lib/scons-3.0.1/SCons/compat/__pycache__/__init__.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/compat/__pycache__/_scons_dbm.cpython-36.pyc
/usr/lib/scons-3.0.1/SCons/compat/_scons_dbm.py
/usr/lib/scons-3.0.1/SCons/compat/_scons_dbm.pyc
/usr/lib/scons-3.0.1/SCons/cpp.py
/usr/lib/scons-3.0.1/SCons/cpp.pyc
/usr/lib/scons-3.0.1/SCons/dblite.py
/usr/lib/scons-3.0.1/SCons/dblite.pyc
/usr/lib/scons-3.0.1/SCons/exitfuncs.py
/usr/lib/scons-3.0.1/SCons/exitfuncs.pyc
/usr/lib/scons-3.0.1/scons-3.0.1-py2.7.egg-info

%files bin
%defattr(-,root,root,-)
/usr/bin/scons
/usr/bin/scons-3.0.1
/usr/bin/scons-configure-cache
/usr/bin/scons-configure-cache-3.0.1
/usr/bin/scons-time
/usr/bin/scons-time-3.0.1
/usr/bin/sconsign
/usr/bin/sconsign-3.0.1

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
