// Tracy Tinfoil build script

using Sharpmake;
using System;
using System.IO;
using System.Collections.Generic;

[Sharpmake.Generate]
public class TracyClient : TinfoilProjectBase
{
	public TracyClient()
	{
		Name = "TracyClient";
		SourceRootPath = @"[project.SharpmakeCsPath]/public";

		SourceFiles.Add("../Tracy.Build.cs");
	}

	[Sharpmake.Configure]
	public void ConfigureAll(Project.Configuration config, TinfoilTarget target)
	{
		config.Output = Configuration.OutputType.Lib;

		config.Options.Add(Options.Vc.Compiler.CppLanguageStandard.CPP17);
		config.Options.Add(Options.Vc.Compiler.ConformanceMode.Enable);
		config.Options.Add(Options.Vc.General.WindowsTargetPlatformVersion.Latest);

		config.IncludePaths.Add(@"[project.SharpmakeCsPath]/public");

		config.Defines.Add("TRACY_ENABLE");
		config.Defines.Add("TRACY_ON_DEMAND");
		config.Defines.Add("TRACY_FIBERS");

		ExcludeFolder(config, target, "client");
		ExcludeFolder(config, target, "common");
		ExcludeFolder(config, target, "libbacktrace");
	}
}
