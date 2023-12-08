"use client";
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  useToast,
  Image,
} from "@chakra-ui/react";
import { useState } from "react";
import axios from "../http-axios";
import { useRouter } from "next/navigation";

export default function Login() {
  const toast = useToast();
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const signup = async () => {
    try {
      const response = await axios.post(
        "/users/",
        {
          name: username,
          email: email,
          password: password,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      await login();
    } catch (error) {
      toast({
        title: "An error occurred.",
        description: "Please try again later.",
        status: "error",
        duration: 9000,
        isClosable: true,
      });
    }
  };
  const login = async () => {
    try {
      const response = await axios.post(
        "/login",
        {
          username: email,
          password: password,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );
      if (response.status === 200) {
        localStorage.setItem("token", response.data.access_token);
        localStorage.setItem("token_type", response.data.token_type);
        toast({
          title: "Successfully Logged In",
          description:
            "You have successfully entered CookIt! Let's start cooking! 🥕",
          status: "success",
          duration: 9000,
          isClosable: true,
        });
        router.push("/dashboard");
      }
    } catch (error) {
      toast({
        title: "An error occurred.",
        description: "Please try again later.",
        status: "error",
        duration: 9000,
        isClosable: true,
      });
    }
  };
  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Box w={{ base: "60%", sm: "60%", md: "50%" }} pl={"12"}>
        <Image
          src="https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2018/12/Shakshuka-19.jpg"
          rounded="1rem"
          shadow="2xl"
          alt="Shakshuka"
        />
      </Box>
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
        <Stack align={"center"}>
          <Text
            fontSize={"xl"}
            fontWeight={"bold"}
            color={"white"}
            bg={"orange.500"}
          >
            Hello, please register to CookIt! 🍳
          </Text>
          <Heading fontSize={"4xl"}>Sign in to your account</Heading>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <FormControl id="name">
              <FormLabel>Name</FormLabel>
              <Input
                type="text"
                placeholder="Your name"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </FormControl>
            <FormControl id="email">
              <FormLabel>Email address</FormLabel>
              <Input
                type="email"
                placeholder="Your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </FormControl>
            <FormControl id="password">
              <FormLabel>Password</FormLabel>
              <Input
                type="password"
                placeholder="Your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </FormControl>
            <Stack spacing={7}>
              <Stack
                direction={{ base: "column", sm: "row" }}
                align={"start"}
                justify={"space-between"}
              ></Stack>
              <Button onClick={signup} colorScheme="orange" variant="solid">
                Sign In
              </Button>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
